

import { useEffect, useState } from "react";
import {
  getLatestSummary,
  getHistory,
  downloadReport,
} from "../api/api";
import { Download, ChevronDown, ChevronUp, TrendingUp, Activity, AlertTriangle, CheckCircle, FileText, Calendar } from "lucide-react";

function Summary() {
  const [latest, setLatest] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [expandedRowId, setExpandedRowId] = useState(null);
  const [downloadingId, setDownloadingId] = useState(null);

  useEffect(() => {
    async function load() {
      try {
        const latestData = await getLatestSummary();
        const historyData = await getHistory();
        setLatest(latestData);
        setHistory(historyData);
      } catch {
        setError("Unable to load summary data.");
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  const toggleRow = (id) => {
    setExpandedRowId((prev) => (prev === id ? null : id));
  };

  const handleDownload = async (id) => {
    try {
      setDownloadingId(id);
      const blob = await downloadReport(id);
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `dataset_report_${id}.pdf`;
      a.click();
      URL.revokeObjectURL(url);
    } catch {
      alert("Download failed");
    } finally {
      setDownloadingId(null);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-600 font-medium">Loading analytics...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center p-6">
        <div className="bg-red-50 border-2 border-red-200 rounded-2xl p-8 max-w-md animate-shake">
          <div className="flex items-center gap-3 mb-3">
            <AlertTriangle className="w-6 h-6 text-red-600" />
            <h3 className="text-lg font-bold text-red-900">Error</h3>
          </div>
          <p className="text-red-700">{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 p-6">
      {/* Animated Background Blobs */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-blue-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob"></div>
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-2000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-indigo-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-4000"></div>
      </div>

      <div className="max-w-7xl mx-auto relative z-10 space-y-8">
        {/* Page Header */}
        <div className="text-center mb-12 animate-fade-in-down">
          <h1 className="text-5xl font-extrabold mb-4">
            <span className="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
              Dataset Summary
            </span>
          </h1>
          <p className="text-gray-600 text-lg">
            Comprehensive analytics and historical data overview
          </p>
        </div>

        {/* Latest Summary Card */}
        {latest && (
          <div className="bg-white/70 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl p-8 hover:shadow-indigo-200/60 transition-all duration-500 animate-fade-in">
            <div className="flex items-center justify-between mb-8">
              <div className="flex items-center gap-4">
                <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg">
                  <TrendingUp className="w-7 h-7 text-white" />
                </div>
                <div>
                  <h2 className="text-2xl font-bold text-gray-900">Latest Summary</h2>
                  <p className="text-sm text-gray-500">Most recent dataset analysis</p>
                </div>
              </div>
              <div className="px-4 py-2 bg-gradient-to-r from-green-50 to-emerald-50 border border-green-200 rounded-xl">
                <span className="text-xs font-bold text-green-700 uppercase">Live Data</span>
              </div>
            </div>

            {/* KPI Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <Stat
                label="Total Equipment"
                value={latest.total_equipment}
                icon={<Activity className="w-5 h-5" />}
                gradient="from-blue-500 to-cyan-500"
              />
              <Stat
                label="Avg Flowrate"
                value={latest.avg_flowrate}
                icon={<TrendingUp className="w-5 h-5" />}
                gradient="from-purple-500 to-pink-500"
              />
              <Stat
                label="Avg Pressure"
                value={latest.avg_pressure}
                icon={<Activity className="w-5 h-5" />}
                gradient="from-orange-500 to-red-500"
              />
              <Stat
                label="Avg Temperature"
                value={latest.avg_temperature}
                icon={<TrendingUp className="w-5 h-5" />}
                gradient="from-emerald-500 to-teal-500"
              />
            </div>

            {/* Health Score Bar */}
            <div className="mt-8 bg-gradient-to-br from-gray-50 to-blue-50/80 rounded-2xl p-6 border border-gray-200">
              <div className="flex items-center justify-between mb-4">
                <p className="text-sm font-bold text-gray-700 uppercase tracking-wide">
                  Overall Health Score
                </p>
                <span className={`text-3xl font-extrabold ${latest.health_score >= 70
                  ? "text-green-600"
                  : latest.health_score >= 40
                    ? "text-amber-600"
                    : "text-red-600"
                  }`}>
                  {latest.health_score}%
                </span>
              </div>

              <div className="relative w-full bg-gray-200 rounded-full h-6 overflow-hidden shadow-inner">
                <div
                  className={`h-6 rounded-full transition-all duration-1000 ease-out ${latest.health_score >= 70
                    ? "bg-gradient-to-r from-green-400 via-green-500 to-emerald-500"
                    : latest.health_score >= 40
                      ? "bg-gradient-to-r from-amber-400 via-amber-500 to-orange-500"
                      : "bg-gradient-to-r from-red-400 via-red-500 to-rose-500"
                    } shadow-lg`}
                  style={{
                    width: `${latest.health_score}%`,
                  }}
                >
                  <div className="absolute inset-0 bg-white opacity-20 animate-pulse"></div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* History Table */}
        <div className="bg-white/70 backdrop-blur-xl border border-white/40 rounded-3xl shadow-2xl overflow-hidden hover:shadow-indigo-200/60 transition-all duration-500 animate-fade-in animation-delay-200">
          <div className="p-8 border-b border-gray-200 bg-gradient-to-r from-blue-50/50 to-indigo-50/50">
            <div className="flex items-center gap-4">
              <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg">
                <FileText className="w-7 h-7 text-white" />
              </div>
              <div>
                <h2 className="text-2xl font-bold text-gray-900">Upload History</h2>
                <p className="text-sm text-gray-500">All previous dataset analyses</p>
              </div>
            </div>
          </div>

          {/* Table */}
          <div className="overflow-x-auto">
            <table className="min-w-full">
              <thead className="bg-gradient-to-r from-gray-50 to-blue-50/30 border-b-2 border-gray-200">
                <tr>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">

                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                    Dataset File
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                    Health Score
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                    Upload Date
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                    Actions
                  </th>
                </tr>
              </thead>

              <tbody className="divide-y divide-gray-100">
                {history.map((item, index) => (
                  <>
                    <tr
                      key={item.id}
                      className="hover:bg-blue-50/50 transition-colors duration-200 animate-fade-in"
                      style={{ animationDelay: `${index * 0.1}s` }}
                    >
                      <td className="px-6 py-4">
                        <button
                          onClick={() => toggleRow(item.id)}
                          className="p-2 hover:bg-indigo-100 rounded-lg transition-all duration-200 transform hover:scale-110"
                        >
                          {expandedRowId === item.id ? (
                            <ChevronUp className="w-5 h-5 text-indigo-600" />
                          ) : (
                            <ChevronDown className="w-5 h-5 text-gray-500" />
                          )}
                        </button>
                      </td>

                      <td className="px-6 py-4">
                        <div className="flex items-center gap-3">
                          <div className="w-10 h-10 bg-gradient-to-br from-blue-100 to-indigo-100 rounded-lg flex items-center justify-center">
                            <FileText className="w-5 h-5 text-blue-600" />
                          </div>
                          <span className="font-medium text-gray-900">{item.file_name}</span>
                        </div>
                      </td>

                      <td className="px-6 py-4">
                        <div className="flex items-center gap-2">
                          <div
                            className={`w-3 h-3 rounded-full ${item.health_score >= 70
                              ? "bg-green-500 animate-pulse"
                              : item.health_score >= 40
                                ? "bg-amber-500 animate-pulse"
                                : "bg-red-500 animate-pulse"
                              }`}
                          ></div>
                          <span
                            className={`font-bold text-lg ${item.health_score >= 70
                              ? "text-green-600"
                              : item.health_score >= 40
                                ? "text-amber-600"
                                : "text-red-600"
                              }`}
                          >
                            {item.health_score}%
                          </span>
                        </div>
                      </td>

                      <td className="px-6 py-4">
                        <div className="flex items-center gap-2 text-gray-600">
                          <Calendar className="w-4 h-4" />
                          <span className="text-sm">
                            {new Date(item.uploaded_at).toLocaleDateString('en-US', {
                              year: 'numeric',
                              month: 'short',
                              day: 'numeric',
                              hour: '2-digit',
                              minute: '2-digit'
                            })}
                          </span>
                        </div>
                      </td>

                      <td className="px-6 py-4">
                        <button
                          onClick={() => handleDownload(item.id)}
                          disabled={downloadingId === item.id}
                          className="group flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-lg font-semibold hover:from-blue-700 hover:to-indigo-700 transition-all duration-300 transform hover:scale-105 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                          {downloadingId === item.id ? (
                            <>
                              <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                              <span className="text-sm">Downloading...</span>
                            </>
                          ) : (
                            <>
                              <Download className="w-4 h-4 group-hover:animate-bounce" />
                              <span className="text-sm">PDF Report</span>
                            </>
                          )}
                        </button>
                      </td>
                    </tr>

                    {/* EXPANDED DETAILS */}
                    {expandedRowId === item.id && (
                      <tr className="bg-gradient-to-br from-blue-50/50 to-indigo-50/30 animate-fade-in">
                        <td colSpan="5" className="px-6 py-6">
                          <CompactDetails summary={item.summary} />
                        </td>
                      </tr>
                    )}
                  </>
                ))}
              </tbody>
            </table>

            {history.length === 0 && (
              <div className="text-center py-16">
                <div className="w-24 h-24 mx-auto mb-4 bg-gradient-to-br from-gray-100 to-gray-200 rounded-full flex items-center justify-center">
                  <FileText className="w-12 h-12 text-gray-400" />
                </div>
                <p className="text-gray-400 font-medium">No upload history found</p>
                <p className="text-gray-400 text-sm mt-2">Start by uploading your first dataset</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

/* ---------- COMPONENTS ---------- */

function Stat({ label, value, icon, gradient }) {
  return (
    <div className="group relative">
      <div className={`absolute -inset-0.5 bg-gradient-to-r ${gradient} rounded-2xl opacity-0 group-hover:opacity-20 blur-xl transition-all duration-500`}></div>

      <div className="relative bg-white border border-gray-200 rounded-2xl p-5 hover:shadow-2xl transition-all duration-300 transform group-hover:scale-105">
        <div className="flex items-start justify-between mb-3">
          <p className="text-xs font-bold text-gray-500 uppercase tracking-wider">
            {label}
          </p>
          <div className={`w-8 h-8 rounded-lg bg-gradient-to-br ${gradient} flex items-center justify-center shadow-md transform group-hover:rotate-12 transition-transform duration-300`}>
            <div className="text-white">
              {icon}
            </div>
          </div>
        </div>
        <p className={`text-3xl font-extrabold bg-gradient-to-r ${gradient} bg-clip-text text-transparent`}>
          {typeof value === 'number' && value % 1 !== 0 ? value.toFixed(1) : value}
        </p>
      </div>
    </div>
  );
}

function CompactDetails({ summary }) {
  const total =
    summary.risk_analysis.high_risk +
    summary.risk_analysis.normal;

  return (
    <div className="space-y-6">
      {/* Averages Section */}
      <div className="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-200">
        <h4 className="text-sm font-bold text-gray-700 uppercase tracking-wider mb-4 flex items-center gap-2">
          <Activity className="w-4 h-4 text-blue-600" />
          Average Parameters
        </h4>
        <div className="grid grid-cols-3 gap-4">
          <div className="text-center">
            <p className="text-xs text-gray-500 mb-1">Flowrate</p>
            <p className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent">
              {summary.averages.flowrate}
            </p>
          </div>
          <div className="text-center">
            <p className="text-xs text-gray-500 mb-1">Pressure</p>
            <p className="text-2xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
              {summary.averages.pressure}
            </p>
          </div>
          <div className="text-center">
            <p className="text-xs text-gray-500 mb-1">Temperature</p>
            <p className="text-2xl font-bold bg-gradient-to-r from-orange-600 to-red-600 bg-clip-text text-transparent">
              {summary.averages.temperature}
            </p>
          </div>
        </div>
      </div>

      {/* Equipment Distribution */}
      <div className="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-200">
        <h4 className="text-sm font-bold text-gray-700 uppercase tracking-wider mb-4 flex items-center gap-2">
          <TrendingUp className="w-4 h-4 text-indigo-600" />
          Equipment Type Distribution
        </h4>
        <div className="flex flex-wrap gap-3">
          {Object.entries(summary.equipment_type_distribution).map(([type, count]) => (
            <div
              key={type}
              className="px-4 py-2 bg-gradient-to-br from-indigo-50 to-blue-50 border border-indigo-200 rounded-xl"
            >
              <span className="text-xs font-semibold text-indigo-900">
                {type}: <span className="text-indigo-600">{count}</span>
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Risk Analysis */}
      <div className="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-200">
        <h4 className="text-sm font-bold text-gray-700 uppercase tracking-wider mb-4 flex items-center gap-2">
          <AlertTriangle className="w-4 h-4 text-amber-600" />
          Risk Analysis
        </h4>
        <div className="grid grid-cols-3 gap-4">
          <InlineBar
            label="High Risk"
            value={summary.risk_analysis.high_risk}
            max={total}
            color="from-red-400 to-rose-500"
            icon={<AlertTriangle className="w-4 h-4" />}
          />
          <InlineBar
            label="Normal"
            value={summary.risk_analysis.normal}
            max={total}
            color="from-green-400 to-emerald-500"
            icon={<CheckCircle className="w-4 h-4" />}
          />
          <InlineBar
            label="Health"
            value={summary.health_score}
            max={100}
            color="from-blue-400 to-indigo-500"
            icon={<Activity className="w-4 h-4" />}
          />
        </div>
      </div>
    </div>
  );
}

function InlineBar({ label, value, max, color, icon }) {
  const percent =
    max > 0 ? Math.min(Math.round((value / max) * 100), 100) : 0;

  return (
    <div className="space-y-2">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div
            className={`w-8 h-8 rounded-lg bg-gradient-to-br ${color} flex items-center justify-center text-white shadow-md`}
          >
            {icon}
          </div>
          <span className="text-sm font-semibold text-gray-700">
            {label}
          </span>
        </div>
        <span className="text-lg font-bold text-gray-900">
          {value}
        </span>
      </div>

      {/* Bar */}
      <div className="w-full bg-gray-200 h-3 rounded-full overflow-hidden shadow-inner">
        <div
          className={`bg-gradient-to-r ${color} h-3 rounded-full shadow-sm`}
          style={{ width: `${percent}%` }}
        />
      </div>
    </div>
  );
}



export default Summary;