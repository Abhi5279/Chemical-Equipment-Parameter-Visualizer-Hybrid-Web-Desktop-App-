

import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { loginUser } from "../api/api";
import {
  LogIn,
  Lock,
  User,
  ArrowRight,
  Sparkles,
  Shield,
  CheckCircle,
  BarChart3,
  TrendingUp,
  Activity,
} from "lucide-react";

function Login() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await loginUser(form);
      localStorage.setItem("token", res.token);
      navigate("/upload");
    } catch (err) {
      setError(
        err.response?.data?.non_field_errors?.[0] ||
        "Invalid username or password. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center p-6 relative overflow-hidden">
      {/* Background blobs (unchanged) */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-blue-300 rounded-full mix-blend-multiply blur-3xl opacity-20 animate-blob" />
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply blur-3xl opacity-20 animate-blob animation-delay-2000" />
        <div className="absolute top-1/2 left-1/2 w-96 h-96 bg-indigo-300 rounded-full mix-blend-multiply blur-3xl opacity-20 animate-blob animation-delay-4000 -translate-x-1/2 -translate-y-1/2" />
      </div>

      <div className="relative z-10 w-full max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-14 items-center">
        {/* LEFT PANEL */}
        <div className="hidden lg:block space-y-8 animate-fade-in-left">
          <div>
            <div className="inline-flex items-center gap-3 px-5 py-2.5 bg-gradient-to-r from-blue-600/10 to-indigo-600/10 border-2 border-blue-600/20 rounded-full backdrop-blur-sm mb-8">
              <Sparkles className="w-5 h-5 text-blue-600" />
              <span className="text-sm font-bold uppercase tracking-wider bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
                Welcome Back
              </span>
            </div>

            <h1 className="text-5xl md:text-6xl font-extrabold mb-6 leading-tight">
              <span className="bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">
                Start Analyzing
              </span>
              <br />
              <span className="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
                Your Equipment Data
              </span>
            </h1>

            <p className="text-xl text-gray-600 leading-relaxed mb-10">
              Join thousands of engineers using our platform to monitor equipment health and prevent costly downtime.
            </p>
          </div>

          {/* Benefits List */}
          <div className="space-y-5">
            <BenefitItem
              icon={<CheckCircle className="w-6 h-6" />}
              title="Instant Analytics"
              description="Upload CSV files and get comprehensive insights immediately"
            />
            <BenefitItem
              icon={<CheckCircle className="w-6 h-6" />}
              title="Professional Reports"
              description="Generate executive-ready PDF reports with one click"
            />
            <BenefitItem
              icon={<CheckCircle className="w-6 h-6" />}
              title="Real-time Monitoring"
              description="Track equipment health scores and risk analysis live"
            />
            <BenefitItem
              icon={<Shield className="w-6 h-6" />}
              title="Secure & Encrypted"
              description="Your data is protected with enterprise-grade security"
            />
          </div>
        </div>

        {/* RIGHT PANEL */}
        <div className="flex flex-col items-center">
          <div className="w-full max-w-md bg-white/80 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl p-10">
            {/* Header */}
            <div className="text-center mb-8">
              <div className="w-16 h-16 mx-auto mb-5 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg">
                <LogIn className="w-8 h-8 text-white" />
              </div>
              <h2 className="text-3xl font-extrabold text-gray-900 mb-2">
                Welcome Back
              </h2>
              <p className="text-gray-600 text-sm">
                Sign in to access your analytics dashboard
              </p>
            </div>

            {/* Form */}
            <form onSubmit={handleSubmit} className="space-y-6">
              <InputField
                label="Username"
                icon={<User />}
                name="username"
                value={form.username}
                onChange={handleChange}
                placeholder="Enter your username"
              />

              <InputField
                label="Password"
                icon={<Lock />}
                name="password"
                type="password"
                value={form.password}
                onChange={handleChange}
                placeholder="Enter your password"
              />

              {error && (
                <div className="p-4 bg-red-50 border border-red-200 rounded-xl text-sm text-red-700 font-medium">
                  {error}
                </div>
              )}

              <button
                type="submit"
                disabled={loading}
                className={`w-full py-4 rounded-xl text-white font-bold text-lg flex items-center justify-center gap-3 transition ${loading
                    ? "bg-gray-300 cursor-not-allowed"
                    : "bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 hover:scale-[1.02]"
                  }`}
              >
                {loading ? "Signing you in..." : <>Sign In <ArrowRight /></>}
              </button>
            </form>

            <div className="mt-8 pt-6 border-t border-gray-200 text-center">
              <p className="text-sm text-gray-600">
                Don’t have an account?{" "}
                <Link to="/register" className="text-blue-600 font-bold hover:underline">
                  Create one
                </Link>
              </p>
            </div>
          </div>

          {/* Trust */}
          <div className="mt-6 flex items-center gap-6 text-sm text-gray-500">
            <span className="flex items-center gap-2">
              <Shield className="w-4 h-4 text-green-600" />
              256-bit Encryption
            </span>
            <span className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-blue-600" />
              ISO Certified
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ---------- SMALL COMPONENTS ---------- */

function InputField({ label, icon, ...props }) {
  return (
    <div>
      <label className="block text-sm font-bold text-gray-700 mb-2 uppercase tracking-wide">
        {label}
      </label>
      <div className="relative">
        <span className="absolute inset-y-0 left-4 flex items-center text-gray-400">
          {icon}
        </span>
        <input
          {...props}
          required
          className="w-full pl-12 pr-4 py-3.5 border-2 border-gray-200 rounded-xl text-sm font-medium focus:outline-none focus:border-blue-600 focus:ring-4 focus:ring-blue-100 bg-white/50"
        />
      </div>
    </div>
  );
}

function StatCard({ icon, value, label, gradient }) {
  return (
    <div className="bg-white/80 border rounded-2xl p-6">
      <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${gradient} flex items-center justify-center text-white mb-4`}>
        {icon}
      </div>
      <p className={`text-3xl font-extrabold bg-gradient-to-r ${gradient} bg-clip-text text-transparent`}>
        {value}
      </p>
      <p className="text-sm text-gray-600 font-medium">{label}</p>
    </div>
  );
}

function FeatureItem({ text }) {
  return (
    <div className="flex items-center gap-3">
      <div className="w-6 h-6 rounded-full bg-gradient-to-br from-green-500 to-emerald-500 flex items-center justify-center">
        <CheckCircle className="w-4 h-4 text-white" />
      </div>
      <p className="text-sm text-gray-700 font-medium">{text}</p>
    </div>
  );
}

// ---------- BENEFIT ITEM COMPONENT ---------- */
function BenefitItem({ icon, title, description }) {
  return (
    <div className="flex items-start gap-4 group">
      <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-green-500 to-emerald-500 flex items-center justify-center flex-shrink-0 shadow-lg group-hover:scale-110 group-hover:rotate-6 transition-all duration-300">
        <div className="text-white">
          {icon}
        </div>
      </div>
      <div>
        <h3 className="font-bold text-gray-900 mb-1">{title}</h3>
        <p className="text-sm text-gray-600 leading-relaxed">{description}</p>
      </div>
    </div>
  );
}

export default Login;
