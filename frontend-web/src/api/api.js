import axios from "axios";

const API_BASE = "http://127.0.0.1:8000/api";

const api = axios.create({
  baseURL: API_BASE,
});

/* ---------- REQUEST INTERCEPTOR ---------- */

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

/* ---------- AUTH ---------- */

export const registerUser = async (data) => {
  const res = await api.post("/register/", data);
  return res.data;
};

export const loginUser = async (data) => {
  const res = await api.post("/login/", data);
  return res.data;
};

/* ---------- CSV ---------- */

export const uploadCSV = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await api.post("/upload/", formData);
  return res.data;
};

/* ---------- DATA ---------- */

export const getLatestSummary = async () => {
  const res = await api.get("/summary/latest/");
  return res.data;
};

export const getHistory = async () => {
  const res = await api.get("/history/");
  return res.data;
};

export const downloadReport = async (id) => {
  const res = await api.get(`/report/${id}/`, {
    responseType: "blob",
  });
  return res.data;
};

/* ---------- AUTH HELPERS ---------- */

export const logout = () => {
  localStorage.removeItem("token");
};
