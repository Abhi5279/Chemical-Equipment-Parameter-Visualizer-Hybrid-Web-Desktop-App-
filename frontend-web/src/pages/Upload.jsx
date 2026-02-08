
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { uploadCSV } from "../api/api";

function Upload() {
  const navigate = useNavigate();

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [overview, setOverview] = useState(null);
  const [isDragging, setIsDragging] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a CSV file to upload.");
      return;
    }

    setError("");
    setLoading(true);

    try {
      const res = await uploadCSV(file);
      setOverview(res.data);
    } catch (err) {
      setError(
        err.response?.data?.error ||
          "Failed to upload CSV. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile && droppedFile.name.endsWith('.csv')) {
      setFile(droppedFile);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 p-6">
      {/* Animated Background Blobs */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-blue-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob"></div>
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-2000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-pink-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-4000"></div>
      </div>

      <div className="max-w-7xl mx-auto relative z-10">
        {/* Page Header */}
        <div className="text-center mb-12 animate-fade-in-down">
          <h1 className="text-5xl md:text-6xl font-extrabold mb-4">
            <span className="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
              Chemical Equipment Analysis
            </span>
          </h1>
          <p className="text-gray-600 text-lg md:text-xl max-w-2xl mx-auto">
            Upload your dataset and unlock powerful insights instantly
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* LEFT PANEL — UPLOAD */}
          <div className="bg-white/70 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl p-8 space-y-6 hover:shadow-indigo-200/60 transition-all duration-500 animate-fade-in-left">
            <div className="flex items-center gap-4">
              <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg transform hover:scale-110 transition-transform duration-300">
                <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
              </div>
              <div>
                <h2 className="text-2xl font-bold text-gray-900">
                  Upload Dataset
                </h2>
                <p className="text-sm text-gray-500">
                  Drag & drop or browse files
                </p>
              </div>
            </div>

            {/* Drag & Drop Zone */}
            <div
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
              className={`relative border-2 border-dashed rounded-2xl p-10 text-center transition-all duration-300 cursor-pointer ${
                isDragging
                  ? "border-blue-500 bg-blue-50 scale-[1.02] shadow-lg"
                  : "border-gray-300 bg-gradient-to-br from-gray-50 to-blue-50/50 hover:border-blue-400 hover:shadow-md"
              }`}
            >
              <input
                type="file"
                accept=".csv"
                onChange={(e) => setFile(e.target.files[0])}
                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
              />

              <div className="relative pointer-events-none">
                <div className={`w-20 h-20 mx-auto mb-4 bg-gradient-to-br from-blue-100 to-indigo-100 rounded-full flex items-center justify-center transition-all duration-300 ${
                  isDragging ? "scale-110 rotate-6" : ""
                }`}>
                  <svg className="w-10 h-10 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>

                {!file ? (
                  <>
                    <p className="text-gray-700 font-semibold mb-2 text-lg">
                      Drop your CSV file here
                    </p>
                    <p className="text-sm text-gray-500">
                      or click to browse from your computer
                    </p>
                  </>
                ) : (
                  <div className="animate-fade-in">
                    <div className="inline-flex items-center gap-3 px-5 py-3 bg-gradient-to-r from-green-50 to-emerald-50 border border-green-200 rounded-xl shadow-sm">
                      <svg className="w-6 h-6 text-green-600" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                      </svg>
                      <span className="text-sm font-semibold text-green-700">{file.name}</span>
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Error Message */}
            {error && (
              <div className="flex items-start gap-3 p-4 bg-red-50 border border-red-200 rounded-xl animate-shake">
                <svg className="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
                <p className="text-sm text-red-700 font-medium">{error}</p>
              </div>
            )}

            {/* Upload Button */}
            <button
              onClick={handleUpload}
              disabled={loading || !file}
              className={`w-full py-4 rounded-xl text-white font-bold text-lg transition-all duration-300 transform shadow-lg ${
                loading || !file
                  ? "bg-gray-300 cursor-not-allowed"
                  : "bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 hover:from-blue-700 hover:via-indigo-700 hover:to-purple-700 hover:shadow-2xl hover:scale-[1.02] active:scale-[0.98]"
              }`}
            >
              {loading ? (
                <span className="flex items-center justify-center gap-3">
                  <svg className="animate-spin h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Analyzing Dataset...
                </span>
              ) : (
                <span className="flex items-center justify-center gap-2">
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                  Upload & Analyze Dataset
                </span>
              )}
            </button>

            {/* Footer Info */}
            <div className="flex items-center justify-between text-xs text-gray-500 pt-4 border-t border-gray-200">
              <span className="flex items-center gap-1.5">
                <svg className="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
                </svg>
                Format: <b className="text-gray-700">.csv</b>
              </span>
              <span className="flex items-center gap-1.5">
                <svg className="w-4 h-4 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                Secure & Encrypted
              </span>
            </div>
          </div>

          {/* RIGHT PANEL — SNAPSHOT */}
          <div className="space-y-6 animate-fade-in-right">
            <div className="bg-white/70 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl p-8 hover:shadow-indigo-200/60 transition-all duration-500">
              <div className="flex items-center justify-between mb-8">
                <div>
                  <h3 className="text-2xl font-bold text-gray-900">
                    Dataset Insights
                  </h3>
                  <p className="text-sm text-gray-500 mt-1">
                    Real-time analytics preview
                  </p>
                </div>
                {overview && (
                  <div className="w-14 h-14 bg-gradient-to-br from-green-400 to-emerald-500 rounded-2xl flex items-center justify-center shadow-lg animate-pulse">
                    <svg className="w-7 h-7 text-white" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  </div>
                )}
              </div>

              {!overview ? (
                <div className="py-20 text-center">
                  <div className="w-28 h-28 mx-auto mb-6 bg-gradient-to-br from-gray-100 to-gray-200 rounded-full flex items-center justify-center">
                    <svg className="w-14 h-14 text-gray-400 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                    </svg>
                  </div>
                  <p className="text-gray-400 font-medium">
                    Upload a dataset to view instant analytics
                  </p>
                  <p className="text-gray-400 text-sm mt-2">
                    Get real-time insights and visualizations
                  </p>
                </div>
              ) : (
                <div className="animate-fade-in">
                  {/* KPI CARDS */}
                  <div className="grid grid-cols-2 gap-4 mb-8">
                    <Kpi 
                      label="Total Equipment" 
                      value={overview.total_equipment}
                      icon="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
                      gradient="from-blue-500 to-cyan-500"
                    />
                    <Kpi 
                      label="Avg Flowrate" 
                      value={overview.avg_flowrate}
                      icon="M13 10V3L4 14h7v7l9-11h-7z"
                      gradient="from-purple-500 to-pink-500"
                    />
                    <Kpi 
                      label="Avg Pressure" 
                      value={overview.avg_pressure}
                      icon="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                      gradient="from-orange-500 to-red-500"
                    />
                    <Kpi 
                      label="Avg Temperature" 
                      value={overview.avg_temperature}
                      icon="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                      gradient="from-emerald-500 to-teal-500"
                    />
                  </div>

                  {/* HEALTH BAR */}
                  <div className="bg-gradient-to-br from-gray-50 to-blue-50/80 rounded-2xl p-6 mb-8 border border-gray-200">
                    <div className="flex items-center justify-between mb-4">
                      <p className="text-sm font-bold text-gray-700 uppercase tracking-wide">
                        Overall Health Score
                      </p>
                      <span className={`text-3xl font-extrabold ${
                        overview.health_score >= 70
                          ? "text-green-600"
                          : overview.health_score >= 40
                          ? "text-amber-600"
                          : "text-red-600"
                      }`}>
                        {overview.health_score}%
                      </span>
                    </div>
                    
                    <div className="relative w-full bg-gray-200 rounded-full h-6 overflow-hidden shadow-inner">
                      <div
                        className={`h-6 rounded-full transition-all duration-1000 ease-out ${
                          overview.health_score >= 70
                            ? "bg-gradient-to-r from-green-400 via-green-500 to-emerald-500"
                            : overview.health_score >= 40
                            ? "bg-gradient-to-r from-amber-400 via-amber-500 to-orange-500"
                            : "bg-gradient-to-r from-red-400 via-red-500 to-rose-500"
                        } shadow-lg`}
                        style={{
                          width: `${overview.health_score}%`,
                        }}
                      >
                        <div className="absolute inset-0 bg-white opacity-20 animate-pulse"></div>
                      </div>
                    </div>
                  </div>

                  {/* ACTION BUTTONS */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <button
                      onClick={() => navigate("/summary")}
                      className="group px-6 py-4 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-xl font-bold hover:from-blue-700 hover:to-indigo-700 transition-all duration-300 transform hover:scale-105 hover:shadow-2xl active:scale-95 flex items-center justify-center gap-2"
                    >
                      <svg className="w-5 h-5 group-hover:rotate-12 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                      </svg>
                      View Summary
                    </button>

                    <button
                      onClick={() => navigate("/analytics")}
                      className="group px-6 py-4 bg-white border-2 border-indigo-200 text-gray-800 rounded-xl font-bold hover:border-indigo-400 hover:bg-indigo-50 transition-all duration-300 transform hover:scale-105 active:scale-95 flex items-center justify-center gap-2 shadow-md hover:shadow-xl"
                    >
                      <svg className="w-5 h-5 group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                      </svg>
                      Analytics
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ---------- COMPONENTS ---------- */

function Kpi({ label, value, icon, gradient }) {
  return (
    <div className="group relative">
      <div className="relative bg-white border border-gray-200 rounded-2xl p-5 hover:border-transparent hover:shadow-2xl transition-all duration-300 transform group-hover:scale-105 overflow-hidden">
        {/* Hover gradient effect */}
        <div className={`absolute inset-0 bg-gradient-to-br ${gradient} opacity-0 group-hover:opacity-5 transition-opacity duration-300`}></div>
        
        <div className="relative flex items-start justify-between">
          <div className="flex-1">
            <p className="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">
              {label}
            </p>
            <p className={`text-3xl font-extrabold bg-gradient-to-r ${gradient} bg-clip-text text-transparent`}>
              {typeof value === 'number' && value % 1 !== 0 ? value.toFixed(1) : value}
            </p>
          </div>
          <div className={`w-11 h-11 rounded-xl bg-gradient-to-br ${gradient} flex items-center justify-center shadow-lg transform group-hover:rotate-12 group-hover:scale-110 transition-all duration-300`}>
            <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d={icon} />
            </svg>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Upload;