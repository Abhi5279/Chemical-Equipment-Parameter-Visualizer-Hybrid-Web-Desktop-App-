

import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { registerUser } from "../api/api";
import { UserPlus, Lock, User, Mail, ArrowRight, Sparkles, Shield, CheckCircle } from "lucide-react";

function Register() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await registerUser(form);
      localStorage.setItem("token", res.token);
      navigate("/upload");
    } catch (err) {
      setError(
        err.response?.data?.username?.[0] ||
          err.response?.data?.password?.[0] ||
          "Registration failed. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center p-6 relative overflow-hidden">
      {/* Animated Background Blobs */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-blue-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-2000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-indigo-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-4000"></div>
      </div>

      <div className="w-full max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center relative z-10">
        {/* LEFT SIDE - Branding & Benefits */}
        <div className="hidden lg:block space-y-8 animate-fade-in-left">
          <div>
            <div className="inline-flex items-center gap-3 px-5 py-2.5 bg-gradient-to-r from-blue-600/10 to-indigo-600/10 border-2 border-blue-600/20 rounded-full backdrop-blur-sm mb-8">
              <Sparkles className="w-5 h-5 text-blue-600" />
              <span className="text-sm font-bold uppercase tracking-wider bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
                Join ChemAnalyze
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

        {/* RIGHT SIDE - Registration Form */}
        <div className="animate-fade-in-right">
          <div className="bg-white/80 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl p-10 hover:shadow-indigo-200/60 transition-all duration-500">
            {/* Header */}
            <div className="text-center mb-8">
              <div className="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg transform hover:scale-110 hover:rotate-6 transition-all duration-300">
                <UserPlus className="w-8 h-8 text-white" />
              </div>
              
              <h2 className="text-3xl font-extrabold text-gray-900 mb-2">
                Create Account
              </h2>
              <p className="text-gray-600">
                Get started with your free account today
              </p>
            </div>

            {/* Form */}
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Username Field */}
              <div className="space-y-2">
                <label className="block text-sm font-bold text-gray-700 uppercase tracking-wide">
                  Username
                </label>
                <div className="relative group">
                  <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <User className="w-5 h-5 text-gray-400 group-focus-within:text-blue-600 transition-colors" />
                  </div>
                  <input
                    type="text"
                    name="username"
                    value={form.username}
                    onChange={handleChange}
                    required
                    placeholder="Enter your username"
                    className="w-full pl-12 pr-4 py-3.5 border-2 border-gray-200 rounded-xl text-sm font-medium focus:outline-none focus:border-blue-600 focus:ring-4 focus:ring-blue-100 transition-all duration-300 bg-white/50"
                  />
                </div>
              </div>

              {/* Password Field */}
              <div className="space-y-2">
                <label className="block text-sm font-bold text-gray-700 uppercase tracking-wide">
                  Password
                </label>
                <div className="relative group">
                  <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <Lock className="w-5 h-5 text-gray-400 group-focus-within:text-blue-600 transition-colors" />
                  </div>
                  <input
                    type="password"
                    name="password"
                    value={form.password}
                    onChange={handleChange}
                    required
                    placeholder="Create a strong password"
                    className="w-full pl-12 pr-4 py-3.5 border-2 border-gray-200 rounded-xl text-sm font-medium focus:outline-none focus:border-blue-600 focus:ring-4 focus:ring-blue-100 transition-all duration-300 bg-white/50"
                  />
                </div>
                <p className="text-xs text-gray-500 flex items-center gap-1.5 mt-2">
                  <Shield className="w-3.5 h-3.5" />
                  Must be at least 8 characters long
                </p>
              </div>

              {/* Error Message */}
              {error && (
                <div className="flex items-start gap-3 p-4 bg-red-50 border-2 border-red-200 rounded-xl animate-shake">
                  <div className="w-5 h-5 rounded-full bg-red-600 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <span className="text-white text-xs font-bold">!</span>
                  </div>
                  <p className="text-sm text-red-700 font-medium">{error}</p>
                </div>
              )}

              {/* Submit Button */}
              <button
                type="submit"
                disabled={loading}
                className={`group w-full py-4 rounded-xl text-white font-bold text-lg transition-all duration-300 transform flex items-center justify-center gap-3 shadow-lg ${
                  loading
                    ? "bg-gray-300 cursor-not-allowed"
                    : "bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 hover:from-blue-700 hover:via-indigo-700 hover:to-purple-700 hover:shadow-2xl hover:scale-[1.02] active:scale-[0.98]"
                }`}
              >
                {loading ? (
                  <>
                    <svg className="animate-spin h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Creating your account...
                  </>
                ) : (
                  <>
                    <span>Create Account</span>
                    <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                  </>
                )}
              </button>

              {/* Terms */}
              <p className="text-xs text-gray-500 text-center">
                By creating an account, you agree to our{" "}
                <a href="#" className="text-blue-600 hover:underline font-semibold">
                  Terms of Service
                </a>{" "}
                and{" "}
                <a href="#" className="text-blue-600 hover:underline font-semibold">
                  Privacy Policy
                </a>
              </p>
            </form>

            {/* Login Link */}
            <div className="mt-8 pt-6 border-t border-gray-200">
              <p className="text-sm text-gray-600 text-center">
                Already have an account?{" "}
                <Link
                  to="/login"
                  className="text-blue-600 hover:text-blue-700 font-bold hover:underline transition-colors"
                >
                  Sign in instead
                </Link>
              </p>
            </div>
          </div>

          {/* Trust Badge */}
          <div className="mt-6 flex items-center justify-center gap-6 text-sm text-gray-500">
            <div className="flex items-center gap-2">
              <Shield className="w-4 h-4 text-green-600" />
              <span>SSL Encrypted</span>
            </div>
            <div className="h-4 w-px bg-gray-300"></div>
            <div className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-blue-600" />
              <span>GDPR Compliant</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ---------- BENEFIT ITEM COMPONENT ---------- */
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

export default Register;