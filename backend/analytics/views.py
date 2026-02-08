
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .models import Dataset
# from .serializers import DatasetSerializer
# from .services.analyzer import analyze_equipment_csv
# from .services.pdf_generator import generate_dataset_pdf
# import os
# from django.http import FileResponse, Http404
# from django.conf import settings
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import AllowAny
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import RegisterSerializer



# class CSVUploadAPIView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request):
#         file = request.FILES.get("file")

#         if not file:
#             return Response(
#                 {"error": "CSV file is required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         summary = analyze_equipment_csv(file)

#         dataset = Dataset.objects.create(
#             file_name=file.name,
#             total_equipment=summary["total_equipment"],
#             avg_flowrate=summary["averages"]["flowrate"],
#             avg_pressure=summary["averages"]["pressure"],
#             avg_temperature=summary["averages"]["temperature"],
#             health_score=summary["health_score"],
#             summary=summary,
#         )

#         serializer = DatasetSerializer(dataset)

#         return Response(
#             {
#                 "message": "CSV analyzed successfully",
#                 "data": serializer.data
#             },
#             status=status.HTTP_201_CREATED
#         )

# class DatasetHistoryAPIView(APIView):
#     """
#     Returns last 5 uploaded datasets
#     """
#     permission_classes = [AllowAny]

#     def get(self, request):
#         datasets = Dataset.objects.order_by("-uploaded_at")[:5]
#         serializer = DatasetSerializer(datasets, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)


# class LatestDatasetSummaryAPIView(APIView):
#     """
#     Returns latest uploaded dataset summary
#     """
#     permission_classes = [AllowAny]

#     def get(self, request):
#         dataset = Dataset.objects.order_by("-uploaded_at").first()

#         if not dataset:
#             return Response(
#                 {"message": "No dataset found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = DatasetSerializer(dataset)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class DatasetPDFReportAPIView(APIView):
#     """
#     Generates and returns PDF report for a dataset
#     """

#     def get(self, request, dataset_id):
#         try:
#             dataset = Dataset.objects.get(id=dataset_id)
#         except Dataset.DoesNotExist:
#             raise Http404("Dataset not found")

#         reports_dir = os.path.join(settings.BASE_DIR, "reports")
#         os.makedirs(reports_dir, exist_ok=True)

#         file_path = os.path.join(
#             reports_dir,
#             f"dataset_report_{dataset.id}.pdf"
#         )

#         generate_dataset_pdf(dataset, file_path)

#         return FileResponse(
#             open(file_path, "rb"),
#             as_attachment=True,
#             filename=f"dataset_report_{dataset.id}.pdf"
#         )


# class RegisterAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         user = serializer.save()

#         token, _ = Token.objects.get_or_create(user=user)

#         return Response(
#             {
#                 "message": "User registered successfully",
#                 "token": token.key
#             },
#             status=status.HTTP_201_CREATED
#         )


import os
from django.http import FileResponse, Http404
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


from .models import Dataset
from .serializers import DatasetSerializer, RegisterSerializer, LoginSerializer
from .services.analyzer import analyze_equipment_csv
from .services.pdf_generator import generate_dataset_pdf


# =========================
# AUTH – REGISTER
# =========================
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": "User registered successfully",
                "token": token.key,
            },
            status=status.HTTP_201_CREATED,
        )
    
# =========================
# AUTH – LOGIN
# =========================

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": "Login successful",
                "token": token.key,
            },
            status=status.HTTP_200_OK,
        )



# =========================
# CSV UPLOAD (USER-SCOPED)
# =========================

class CSVUploadAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "CSV file is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # ✅ Analyze CSV
        summary = analyze_equipment_csv(file)

        # ✅ Save dataset (summary is a DICT)
        dataset = Dataset.objects.create(
            user=request.user,
            file_name=file.name,
            total_equipment=summary["total_equipment"],
            avg_flowrate=summary["averages"]["flowrate"],
            avg_pressure=summary["averages"]["pressure"],
            avg_temperature=summary["averages"]["temperature"],
            health_score=summary["health_score"],
            summary=summary,  # ✅ THIS IS THE KEY LINE
        )

        serializer = DatasetSerializer(dataset)

        return Response(
            {
                "message": "CSV analyzed successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


# =========================
# HISTORY (LAST 5 – USER ONLY)
# =========================
class DatasetHistoryAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("AUTH HEADER:", request.headers.get("Authorization"))
        print("USER:", request.user)
        datasets = (
            Dataset.objects.filter(user=request.user)
            .order_by("-uploaded_at")[:5]
        )

        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# =========================
# LATEST SUMMARY (USER ONLY)
# =========================
class LatestDatasetSummaryAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dataset = (
            Dataset.objects.filter(user=request.user)
            .order_by("-uploaded_at")
            .first()
        )

        if not dataset:
            return Response(
                {"message": "No dataset found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = DatasetSerializer(dataset)
        return Response(serializer.data, status=status.HTTP_200_OK)


# =========================
# PDF REPORT (SECURE)
# =========================
class DatasetPDFReportAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id):
        try:
            dataset = Dataset.objects.get(
                id=dataset_id,
                user=request.user,
            )
        except Dataset.DoesNotExist:
            raise Http404("Dataset not found")

        reports_dir = os.path.join(settings.BASE_DIR, "reports")
        os.makedirs(reports_dir, exist_ok=True)

        file_path = os.path.join(
            reports_dir,
            f"dataset_report_{dataset.id}.pdf"
        )

        generate_dataset_pdf(dataset, file_path)

        return FileResponse(
            open(file_path, "rb"),
            as_attachment=True,
            filename=f"dataset_report_{dataset.id}.pdf",
        )
