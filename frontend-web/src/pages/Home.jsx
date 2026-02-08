

import { useNavigate } from "react-router-dom";
import { Upload, BarChart3, Activity, FileText, TrendingUp, Shield } from "lucide-react";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 relative overflow-hidden">
      {/* Animated Background Blobs */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-blue-300 rounded-full mix-blend-multiply filter blur-3xl opacity-25 animate-blob"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-25 animate-blob animation-delay-2000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-indigo-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-4000"></div>
      </div>

      {/* --- HERO SECTION --- */}
      <section className="relative flex-grow flex flex-col items-center justify-center px-6 py-28 text-center">
        <div className="max-w-6xl mx-auto z-10">
          {/* Badge */}
          <div className="inline-block px-6 py-2.5 mb-10 text-sm font-bold tracking-widest uppercase bg-gradient-to-r from-blue-600/10 to-indigo-600/10 border-2 border-blue-600/20 rounded-full backdrop-blur-md animate-fade-in-down">
            <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              ⚡ Precision Engineering Dashboard
            </span>
          </div>
          
          {/* Main Heading */}
          <h1 className="text-6xl md:text-7xl font-extrabold leading-tight mb-8 animate-fade-in">
            <span className="bg-gradient-to-r from-gray-900 via-blue-900 to-indigo-900 bg-clip-text text-transparent">
              Chemical Equipment
            </span>
            <br />
            <span className="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
              Analytics Platform
            </span>
          </h1>

          {/* Subheading */}
          <p className="mt-8 text-xl md:text-2xl text-gray-600 max-w-4xl mx-auto leading-relaxed animate-fade-in animation-delay-200">
            Transform raw operational data into actionable intelligence. 
            <span className="font-semibold text-blue-700"> Analyze flowrates and pressures</span> to generate 
            <span className="font-semibold text-indigo-700"> professional reports</span> instantly.
          </p>

          {/* CTA Buttons */}
          <div className="mt-14 flex flex-col sm:flex-row gap-6 justify-center animate-fade-in animation-delay-400">
            <button
              onClick={() => navigate("/upload")}
              className="group px-12 py-6 bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white rounded-2xl text-xl font-bold hover:shadow-2xl hover:shadow-blue-500/50 transform hover:scale-105 hover:-translate-y-1 transition-all duration-300 flex items-center justify-center gap-4"
            >
              <Upload className="w-7 h-7 group-hover:rotate-12 transition-transform" />
              Start Analysis Engine
            </button>
            
            <button  
              onClick={() => navigate("/summary")}
              className="px-12 py-6 bg-white/80 backdrop-blur-md border-2 border-indigo-200 text-gray-800 rounded-2xl text-xl font-bold hover:bg-indigo-50 hover:border-indigo-400 transition-all duration-300 transform hover:scale-105 shadow-xl flex items-center justify-center gap-4"
            >
              <BarChart3 className="w-7 h-7" />
              View Dashboard
            </button>
          </div>
        </div>
      </section>

      {/* --- FEATURES GRID --- */}
      <section className="relative py-28 px-6 bg-white/60 backdrop-blur-md">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-20 animate-fade-in">
            <h2 className="text-5xl font-extrabold mb-6 text-gray-900">
              Powerful Analytics Features
            </h2>
            <p className="text-gray-600 text-xl max-w-3xl mx-auto">
              Everything you need to monitor, analyze, and optimize your chemical equipment operations.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            <FeatureCard
              icon={<Activity className="w-8 h-8" />}
              gradient="from-blue-500 to-cyan-500"
              title="Real-time Metrics"
              description="Track equipment count, average flowrate, and pressure with live updates and instant calculations."
              delay="0"
            />
            <FeatureCard
              icon={<TrendingUp className="w-8 h-8" />}
              gradient="from-emerald-500 to-teal-500"
              title="Health Scoring"
              description="Automated algorithms analyze parameters to calculate comprehensive health scores (0-100%)."
              delay="200"
            />
            <FeatureCard
              icon={<Shield className="w-8 h-8" />}
              gradient="from-indigo-500 to-purple-500"
              title="Risk Assessment"
              description="Advanced systems identify high-risk equipment based on operational thresholds."
              delay="400"
            />
            <FeatureCard
              icon={<Upload className="w-8 h-8" />}
              gradient="from-orange-500 to-red-500"
              title="CSV Processing"
              description="Upload large-scale logs instantly with intelligent validation and automated cleaning."
              delay="600"
            />
            <FeatureCard
              icon={<FileText className="w-8 h-8" />}
              gradient="from-rose-500 to-pink-500"
              title="Professional Reports"
              description="Generate executive-ready PDF reports with KPI summaries and visual health bars."
              delay="800"
            />
            <FeatureCard
              icon={<BarChart3 className="w-8 h-8" />}
              gradient="from-purple-500 to-pink-500"
              title="Type Distribution"
              description="Visual breakdown of equipment by type with detailed count analysis and charts."
              delay="1000"
            />
          </div>
        </div>
      </section>

      {/* --- FOOTER --- */}
      <footer className="relative bg-slate-900 border-t border-white/10 py-16 px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-10">
          <div>
            <h2 className="text-white font-extrabold text-3xl tracking-tight">
              CHEM<span className="bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">ANALYZE</span>
            </h2>
            <p className="text-gray-400 text-sm mt-3">Industrial-grade analytics platform.</p>
          </div>
          
          <div className="flex gap-10 text-gray-400 font-medium">
            <a href="#" className="hover:text-blue-400 transition-colors">Features</a>
            <a href="#" className="hover:text-blue-400 transition-colors">Docs</a>
            <a href="#" className="hover:text-blue-400 transition-colors">Support</a>
          </div>

          <p className="text-gray-500 text-sm">
            © 2026 ChemAnalyze Systems. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}

function FeatureCard({ icon, gradient, title, description, delay }) {
  return (
    <div className={`group relative animate-fade-in animation-delay-${delay}`}>
      <div className={`absolute -inset-1 bg-gradient-to-r ${gradient} rounded-3xl opacity-0 group-hover:opacity-20 blur-2xl transition-all duration-500`}></div>
      <div className="relative bg-white/90 backdrop-blur-md border border-gray-200 rounded-3xl p-10 hover:shadow-2xl transition-all duration-500 transform group-hover:scale-[1.03] h-full flex flex-col items-center text-center">
        <div className={`w-16 h-16 bg-gradient-to-br ${gradient} rounded-2xl flex items-center justify-center mb-8 shadow-xl text-white transform group-hover:rotate-6 transition-transform`}>
          {icon}
        </div>
        <h3 className="text-2xl font-bold text-gray-900 mb-4">{title}</h3>
        <p className="text-gray-600 text-lg leading-relaxed">{description}</p>
      </div>
    </div>
  );
}

export default Home;