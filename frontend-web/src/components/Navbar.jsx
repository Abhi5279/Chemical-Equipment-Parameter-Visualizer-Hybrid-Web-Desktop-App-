
import { NavLink, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { Menu, X, LogOut, LayoutDashboard, Database, FileBarChart, Home, Sparkles } from "lucide-react";

function Navbar() {
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    setIsAuthenticated(!!token);

    // Scroll effect for navbar
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setIsAuthenticated(false);
    setIsOpen(false);
    navigate("/login");
  };

  const toggleMenu = () => setIsOpen(!isOpen);

  const baseLinkClass = "px-4 py-2.5 rounded-xl text-sm font-bold transition-all duration-300 flex items-center gap-2 relative overflow-hidden group";
  
  const getLinkStyle = (isActive) => 
    isActive 
      ? `${baseLinkClass} bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-lg shadow-blue-500/30 scale-105` 
      : `${baseLinkClass} text-gray-700 hover:text-blue-600 hover:bg-blue-50`;

  return (
    <nav className={`sticky top-0 z-50 transition-all duration-500 ${
      scrolled 
        ? 'bg-white/90 backdrop-blur-xl shadow-xl border-b border-gray-200' 
        : 'bg-white/70 backdrop-blur-md border-b border-gray-100'
    }`}>
      {/* Gradient top border */}
      <div className="h-1 bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600"></div>
      
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-20 items-center">
          
          {/* --- BRAND --- */}
          <div 
            className="group flex items-center gap-3 cursor-pointer animate-fade-in" 
            onClick={() => navigate("/")}
          >
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-2xl blur opacity-50 group-hover:opacity-75 transition-opacity"></div>
              <div className="relative w-12 h-12 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 shadow-lg">
                <Sparkles className="w-6 h-6 text-white" />
              </div>
            </div>
            <span className="text-2xl font-extrabold tracking-tight">
              <span className="bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">CHEM</span>
              <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">ANALYZE</span>
            </span>
          </div>

          {/* --- DESKTOP NAV --- */}
          <div className="hidden md:flex items-center space-x-2 animate-fade-in animation-delay-200">
            <NavLink to="/" className={({ isActive }) => getLinkStyle(isActive)}>
              <Home size={18} />
              <span>Home</span>
              {({ isActive }) => isActive && (
                <span className="absolute inset-0 bg-gradient-to-r from-blue-600 to-indigo-600 opacity-0 group-hover:opacity-10 transition-opacity"></span>
              )}
            </NavLink>
            
            {isAuthenticated && (
              <>
                <NavLink to="/upload" className={({ isActive }) => getLinkStyle(isActive)}>
                  <Database size={18} />
                  <span>Upload</span>
                </NavLink>
                <NavLink to="/summary" className={({ isActive }) => getLinkStyle(isActive)}>
                  <FileBarChart size={18} />
                  <span>Summary</span>
                </NavLink>
                <NavLink to="/analytics" className={({ isActive }) => getLinkStyle(isActive)}>
                  <LayoutDashboard size={18} />
                  <span>Analytics</span>
                </NavLink>
              </>
            )}

            {/* Divider */}
            <div className="h-8 w-[2px] bg-gradient-to-b from-transparent via-gray-300 to-transparent mx-3"></div>

            {!isAuthenticated ? (
              <div className="flex gap-3">
                <NavLink 
                  to="/login" 
                  className="px-6 py-2.5 rounded-xl text-sm font-bold text-gray-700 hover:text-blue-600 hover:bg-blue-50 transition-all duration-300"
                >
                  Login
                </NavLink>
                <NavLink 
                  to="/register" 
                  className="group px-6 py-2.5 rounded-xl text-sm font-bold bg-gradient-to-r from-blue-600 to-indigo-600 text-white hover:from-blue-700 hover:to-indigo-700 transition-all duration-300 shadow-lg shadow-blue-500/30 hover:shadow-xl hover:scale-105 transform relative overflow-hidden"
                >
                  <span className="relative z-10">Join Now</span>
                  <div className="absolute inset-0 bg-white opacity-0 group-hover:opacity-20 transition-opacity"></div>
                </NavLink>
              </div>
            ) : (
              <button
                onClick={handleLogout}
                className="group flex items-center gap-2 px-5 py-2.5 text-sm font-bold text-red-600 hover:text-white hover:bg-red-600 rounded-xl transition-all duration-300 border-2 border-red-200 hover:border-red-600 hover:shadow-lg hover:scale-105 transform"
              >
                <LogOut size={18} className="group-hover:rotate-12 transition-transform" />
                <span>Logout</span>
              </button>
            )}
          </div>

          {/* --- MOBILE TOGGLE BUTTON --- */}
          <div className="md:hidden flex items-center">
            <button 
              onClick={toggleMenu} 
              className={`p-3 rounded-xl transition-all duration-300 transform ${
                isOpen 
                  ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white scale-110 rotate-90' 
                  : 'text-gray-700 hover:bg-blue-50 hover:text-blue-600'
              }`}
            >
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* --- MOBILE MENU (SLIDE DOWN WITH ANIMATION) --- */}
      <div className={`md:hidden overflow-hidden transition-all duration-500 ease-in-out ${
        isOpen ? 'max-h-screen opacity-100' : 'max-h-0 opacity-0'
      }`}>
        <div className="px-4 pt-4 pb-8 space-y-3 bg-gradient-to-b from-blue-50/50 to-white border-t border-gray-200">
          <NavLink 
            to="/" 
            onClick={() => setIsOpen(false)} 
            className={({ isActive }) => `${getLinkStyle(isActive)} w-full justify-start`}
          >
            <Home size={20} />
            <span>Home</span>
          </NavLink>
          
          {isAuthenticated && (
            <>
              <NavLink 
                to="/upload" 
                onClick={() => setIsOpen(false)} 
                className={({ isActive }) => `${getLinkStyle(isActive)} w-full justify-start`}
              >
                <Database size={20} />
                <span>Upload Dataset</span>
              </NavLink>
              <NavLink 
                to="/summary" 
                onClick={() => setIsOpen(false)} 
                className={({ isActive }) => `${getLinkStyle(isActive)} w-full justify-start`}
              >
                <FileBarChart size={20} />
                <span>Summary</span>
              </NavLink>
              <NavLink 
                to="/analytics" 
                onClick={() => setIsOpen(false)} 
                className={({ isActive }) => `${getLinkStyle(isActive)} w-full justify-start`}
              >
                <LayoutDashboard size={20} />
                <span>Analytics Dashboard</span>
              </NavLink>
            </>
          )}

          {/* Divider */}
          <div className="h-[2px] bg-gradient-to-r from-transparent via-gray-300 to-transparent my-4"></div>

          {!isAuthenticated ? (
            <div className="flex flex-col gap-3 pt-2">
              <NavLink 
                to="/login" 
                onClick={() => setIsOpen(false)} 
                className="w-full text-center py-3.5 bg-white border-2 border-blue-200 text-blue-700 rounded-xl font-bold hover:bg-blue-50 hover:border-blue-400 transition-all duration-300 shadow-md"
              >
                Login to Account
              </NavLink>
              <NavLink 
                to="/register" 
                onClick={() => setIsOpen(false)} 
                className="w-full text-center py-3.5 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-xl font-bold shadow-lg shadow-blue-500/30 hover:shadow-xl hover:scale-105 transition-all duration-300"
              >
                Create Account
              </NavLink>
            </div>
          ) : (
            <button
              onClick={handleLogout}
              className="w-full flex items-center justify-center gap-3 py-3.5 text-white font-bold bg-gradient-to-r from-red-600 to-rose-600 rounded-xl shadow-lg hover:shadow-xl hover:scale-105 transition-all duration-300 mt-2"
            >
              <LogOut size={20} />
              <span>Logout</span>
            </button>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;