
import { useEffect, useState } from "react";
import { getHistory } from "../api/api";
import {
  Chart as ChartJS,
  BarElement,
  ArcElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
} from "chart.js";
import { Bar, Doughnut, Line } from "react-chartjs-2";
import {
  Activity,
  TrendingUp,
  AlertTriangle,
  CheckCircle,
  Zap,
  BarChart3,
  PieChart,
  LineChart,
  Gauge,
  ArrowUpRight,
  ArrowDownRight,
} from "lucide-react";

ChartJS.register(
  BarElement,
  ArcElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  PointElement,
  LineElement
);

function Analytics() {
  const [datasets, setDatasets] = useState([]);
  const [selected, setSelected] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const history = await getHistory();
        setDatasets(history);
        setSelected(history[0] || null);
      } catch (error) {
        console.error("Failed to load analytics", error);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <div className="w-20 h-20 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mx-auto mb-6"></div>
          <p className="text-gray-600 font-semibold text-lg">Loading analytics dashboard...</p>
        </div>
      </div>
    );
  }

  if (!selected) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center p-6">
        <div className="bg-white/80 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl p-12 text-center max-w-md">
          <div className="w-24 h-24 mx-auto mb-6 bg-gradient-to-br from-gray-100 to-gray-200 rounded-full flex items-center justify-center">
            <BarChart3 className="w-12 h-12 text-gray-400" />
          </div>
          <h3 className="text-2xl font-bold text-gray-900 mb-2">No Data Available</h3>
          <p className="text-gray-600">Upload a dataset to view analytics</p>
        </div>
      </div>
    );
  }

  /* ---------------- CHART CONFIGURATIONS ---------------- */

  const equipmentChart = {
    labels: Object.keys(selected.summary.equipment_type_distribution),
    datasets: [
      {
        label: "Equipment Count",
        data: Object.values(selected.summary.equipment_type_distribution),
        backgroundColor: [
          "rgba(59, 130, 246, 0.8)",
          "rgba(99, 102, 241, 0.8)",
          "rgba(139, 92, 246, 0.8)",
          "rgba(168, 85, 247, 0.8)",
          "rgba(236, 72, 153, 0.8)",
        ],
        borderColor: [
          "rgb(59, 130, 246)",
          "rgb(99, 102, 241)",
          "rgb(139, 92, 246)",
          "rgb(168, 85, 247)",
          "rgb(236, 72, 153)",
        ],
        borderWidth: 2,
        borderRadius: 8,
      },
    ],
  };

  const riskChart = {
    labels: ["High Risk", "Normal"],
    datasets: [
      {
        data: [
          selected.summary.risk_analysis.high_risk,
          selected.summary.risk_analysis.normal,
        ],
        backgroundColor: [
          "rgba(239, 68, 68, 0.8)",
          "rgba(34, 197, 94, 0.8)",
        ],
        borderColor: ["rgb(239, 68, 68)", "rgb(34, 197, 94)"],
        borderWidth: 3,
      },
    ],
  };

  const metricsChart = {
    labels: ["Flowrate", "Pressure", "Temperature"],
    datasets: [
      {
        label: "Average Metrics",
        data: [
          selected.avg_flowrate,
          selected.avg_pressure,
          selected.avg_temperature,
        ],
        borderColor: "rgb(37, 99, 235)",
        backgroundColor: "rgba(147, 197, 253, 0.5)",
        tension: 0.4,
        fill: true,
        borderWidth: 3,
        pointRadius: 6,
        pointBackgroundColor: "rgb(37, 99, 235)",
        pointBorderColor: "#fff",
        pointBorderWidth: 2,
        pointHoverRadius: 8,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: true,
        position: "top",
        labels: {
          usePointStyle: true,
          padding: 15,
          font: {
            size: 12,
            weight: "600",
          },
        },
      },
      tooltip: {
        backgroundColor: "rgba(0, 0, 0, 0.8)",
        padding: 12,
        cornerRadius: 8,
        titleFont: {
          size: 14,
          weight: "bold",
        },
        bodyFont: {
          size: 13,
        },
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: {
          color: "rgba(0, 0, 0, 0.05)",
        },
      },
      x: {
        grid: {
          display: false,
        },
      },
    },
  };

  const riskPercentage = Math.round(
    (selected.summary.risk_analysis.high_risk /
      (selected.summary.risk_analysis.high_risk + selected.summary.risk_analysis.normal)) *
      100
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 p-6">
      {/* Animated Background Blobs */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-blue-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-2000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-indigo-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-4000"></div>
      </div>

      <div className="max-w-[1800px] mx-auto relative z-10">
        {/* Page Header */}
        <div className="text-center mb-12 animate-fade-in-down">
          <div className="inline-flex items-center gap-3 px-6 py-3 bg-gradient-to-r from-blue-600/10 to-indigo-600/10 border-2 border-blue-600/20 rounded-full backdrop-blur-sm mb-6">
            <BarChart3 className="w-5 h-5 text-blue-600" />
            <span className="text-sm font-bold uppercase tracking-wider bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              Advanced Analytics
            </span>
          </div>
          <h1 className="text-5xl md:text-6xl font-extrabold mb-4">
            <span className="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
              Analytics Dashboard
            </span>
          </h1>
          <p className="text-gray-600 text-lg max-w-2xl mx-auto">
            Comprehensive visual insights and real-time equipment monitoring
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
          {/* LEFT SIDEBAR - Dataset Selector */}
          <div className="lg:col-span-1 animate-fade-in-left">
            <div className="bg-white/70 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl p-6 sticky top-6">
              <div className="flex items-center gap-3 mb-6">
                <div className="w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg">
                  <Activity className="w-6 h-6 text-white" />
                </div>
                <div>
                  <h2 className="text-lg font-bold text-gray-900">Datasets</h2>
                  <p className="text-xs text-gray-500">Select to analyze</p>
                </div>
              </div>

              <div className="space-y-3 max-h-[600px] overflow-y-auto pr-2 custom-scrollbar">
                {datasets.map((item, index) => (
                  <button
                    key={item.id}
                    onClick={() => setSelected(item)}
                    className={`w-full text-left p-4 rounded-2xl border-2 transition-all duration-300 transform hover:scale-[1.02] ${
                      selected.id === item.id
                        ? "border-blue-500 bg-gradient-to-br from-blue-50 to-indigo-50 shadow-lg"
                        : "border-gray-200 bg-white/50 hover:bg-white hover:shadow-md"
                    }`}
                    style={{ animationDelay: `${index * 0.1}s` }}
                  >
                    <div className="flex items-start justify-between mb-2">
                      <p className="text-sm font-bold text-gray-900">
                        {item.file_name}
                      </p>
                      {selected.id === item.id && (
                        <CheckCircle className="w-5 h-5 text-blue-600" />
                      )}
                    </div>
                    <p className="text-xs text-gray-500 mb-3">
                      ID: {item.id} • User: {item.user}
                    </p>
                    <div className="flex items-center gap-2">
                      <div
                        className={`w-2 h-2 rounded-full ${
                          item.health_score >= 70
                            ? "bg-green-500 animate-pulse"
                            : item.health_score >= 40
                            ? "bg-amber-500 animate-pulse"
                            : "bg-red-500 animate-pulse"
                        }`}
                      ></div>
                      <span
                        className={`text-sm font-bold ${
                          item.health_score >= 70
                            ? "text-green-600"
                            : item.health_score >= 40
                            ? "text-amber-600"
                            : "text-red-600"
                        }`}
                      >
                        Health: {item.health_score}%
                      </span>
                    </div>
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* RIGHT PANEL - Analytics */}
          <div className="lg:col-span-3 space-y-8 animate-fade-in-right">
            {/* Dataset Info Header */}
            <div className="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 rounded-3xl shadow-2xl p-8 text-white">
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h2 className="text-3xl font-extrabold mb-2">
                    {selected.file_name}
                  </h2>
                  <p className="text-blue-100 text-sm flex items-center gap-2">
                    <Activity className="w-4 h-4" />
                    Uploaded: {new Date(selected.uploaded_at).toLocaleString()}
                  </p>
                </div>
                <div className="text-right">
                  <p className="text-sm text-blue-100 mb-1">Overall Health</p>
                  <p className="text-5xl font-extrabold">{selected.health_score}%</p>
                </div>
              </div>
            </div>

            {/* KPI CARDS */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">
              <KpiCard
                label="Total Equipment"
                value={selected.total_equipment}
                icon={<Activity className="w-7 h-7" />}
                gradient="from-blue-500 to-cyan-500"
                trend="+12%"
                trendUp={true}
              />
              <KpiCard
                label="Avg Flowrate"
                value={selected.avg_flowrate}
                icon={<Zap className="w-7 h-7" />}
                gradient="from-purple-500 to-pink-500"
                trend="+5%"
                trendUp={true}
              />
              <KpiCard
                label="Avg Pressure"
                value={selected.avg_pressure}
                icon={<Gauge className="w-7 h-7" />}
                gradient="from-orange-500 to-red-500"
                trend="-3%"
                trendUp={false}
              />
              <KpiCard
                label="Avg Temperature"
                value={selected.avg_temperature}
                icon={<TrendingUp className="w-7 h-7" />}
                gradient="from-emerald-500 to-teal-500"
                trend="+8%"
                trendUp={true}
              />
            </div>

            {/* Risk Overview Banner */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-gradient-to-br from-red-50 to-rose-50 border-2 border-red-200 rounded-3xl p-6 shadow-lg">
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-12 h-12 bg-red-500 rounded-xl flex items-center justify-center shadow-lg">
                    <AlertTriangle className="w-6 h-6 text-white" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-red-900">High Risk Equipment</h3>
                    <p className="text-sm text-red-600">Requires immediate attention</p>
                  </div>
                </div>
                <div className="flex items-end gap-4">
                  <p className="text-5xl font-extrabold text-red-600">
                    {selected.summary.risk_analysis.high_risk}
                  </p>
                  <p className="text-2xl font-bold text-red-400 mb-2">
                    {riskPercentage}%
                  </p>
                </div>
              </div>

              <div className="bg-gradient-to-br from-green-50 to-emerald-50 border-2 border-green-200 rounded-3xl p-6 shadow-lg">
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-12 h-12 bg-green-500 rounded-xl flex items-center justify-center shadow-lg">
                    <CheckCircle className="w-6 h-6 text-white" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-green-900">Normal Equipment</h3>
                    <p className="text-sm text-green-600">Operating optimally</p>
                  </div>
                </div>
                <div className="flex items-end gap-4">
                  <p className="text-5xl font-extrabold text-green-600">
                    {selected.summary.risk_analysis.normal}
                  </p>
                  <p className="text-2xl font-bold text-green-400 mb-2">
                    {100 - riskPercentage}%
                  </p>
                </div>
              </div>
            </div>

            {/* CHARTS ROW 1 */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <ChartCard
                title="Equipment Type Distribution"
                icon={<BarChart3 className="w-6 h-6" />}
                gradient="from-blue-500 to-indigo-500"
              >
                <Bar data={equipmentChart} options={chartOptions} />
              </ChartCard>

              <ChartCard
                title="Risk Analysis Breakdown"
                icon={<PieChart className="w-6 h-6" />}
                gradient="from-purple-500 to-pink-500"
              >
                <div className="h-[300px] flex items-center justify-center">
                  <Doughnut data={riskChart} options={{ ...chartOptions, maintainAspectRatio: false }} />
                </div>
              </ChartCard>
            </div>

            {/* CHART ROW 2 - Full Width */}
            <ChartCard
              title="Average Metrics Overview"
              icon={<LineChart className="w-6 h-6" />}
              gradient="from-emerald-500 to-teal-500"
              fullWidth
            >
              <Line data={metricsChart} options={chartOptions} />
            </ChartCard>

            {/* Equipment Type Details Table */}
            <div className="bg-white/70 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl overflow-hidden">
              <div className="bg-gradient-to-r from-indigo-50 to-blue-50 border-b border-gray-200 p-6">
                <h3 className="text-xl font-bold text-gray-900 flex items-center gap-3">
                  <Activity className="w-6 h-6 text-indigo-600" />
                  Equipment Distribution Details
                </h3>
              </div>
              <div className="p-6">
                <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                  {Object.entries(selected.summary.equipment_type_distribution).map(
                    ([type, count], index) => (
                      <div
                        key={type}
                        className="bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-blue-200 rounded-2xl p-5 hover:shadow-xl transition-all duration-300 transform hover:scale-105 animate-fade-in"
                        style={{ animationDelay: `${index * 0.1}s` }}
                      >
                        <p className="text-sm font-semibold text-gray-600 mb-2 uppercase tracking-wide">
                          {type}
                        </p>
                        <p className="text-4xl font-extrabold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
                          {count}
                        </p>
                      </div>
                    )
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

/* --------- COMPONENTS --------- */

function KpiCard({ label, value, icon, gradient, trend, trendUp }) {
  return (
    <div className="group relative animate-fade-in">
      <div
        className={`absolute -inset-0.5 bg-gradient-to-r ${gradient} rounded-3xl opacity-0 group-hover:opacity-30 blur-xl transition-all duration-500`}
      ></div>

      <div className="relative bg-white/80 backdrop-blur-sm border border-gray-200 rounded-3xl p-6 hover:shadow-2xl transition-all duration-300 transform group-hover:scale-105">
        <div className="flex items-start justify-between mb-4">
          <div className="flex-1">
            <p className="text-xs font-bold text-gray-500 uppercase tracking-wider mb-3">
              {label}
            </p>
            <p
              className={`text-4xl font-extrabold bg-gradient-to-r ${gradient} bg-clip-text text-transparent`}
            >
              {typeof value === "number" && value % 1 !== 0 ? value.toFixed(1) : value}
            </p>
          </div>
          <div
            className={`w-14 h-14 rounded-2xl bg-gradient-to-br ${gradient} flex items-center justify-center shadow-lg transform group-hover:rotate-12 group-hover:scale-110 transition-all duration-300`}
          >
            <div className="text-white">{icon}</div>
          </div>
        </div>
        <div className="flex items-center gap-2 mt-3">
          {trendUp ? (
            <ArrowUpRight className="w-4 h-4 text-green-600" />
          ) : (
            <ArrowDownRight className="w-4 h-4 text-red-600" />
          )}
          <span
            className={`text-sm font-bold ${
              trendUp ? "text-green-600" : "text-red-600"
            }`}
          >
            {trend}
          </span>
          <span className="text-xs text-gray-500">vs last period</span>
        </div>
      </div>
    </div>
  );
}

function ChartCard({ title, icon, gradient, children, fullWidth }) {
  return (
    <div
      className={`bg-white/70 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl overflow-hidden hover:shadow-indigo-200/60 transition-all duration-500 ${
        fullWidth ? "col-span-full" : ""
      }`}
    >
      <div className={`bg-gradient-to-r ${gradient} p-6 border-b border-white/20`}>
        <h3 className="text-xl font-bold text-white flex items-center gap-3">
          <div className="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
            {icon}
          </div>
          {title}
        </h3>
      </div>
      <div className="p-8">{children}</div>
    </div>
  );
}

export default Analytics;