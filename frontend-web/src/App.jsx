

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Upload from "./pages/Upload";
import Summary from "./pages/Summary";
import Analytics from "./pages/Analytics";
import Login from "./pages/Login";
import Register from "./pages/Register";

function App() {
    return (
        <Router>
            <div className="min-h-screen bg-[#F8F9FA] flex flex-col font-sans antialiased">
                <Navbar />
                <main className="flex-grow flex flex-col">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/upload" element={<PageContainer><Upload /></PageContainer>} />
                        <Route path="/summary" element={<PageContainer><Summary /></PageContainer>} />
                        <Route path="/analytics" element={<PageContainer><Analytics /></PageContainer>} />
                        {/* Auth pages often look better in a centered, focused view */}
                        <Route path="/login" element={<AuthContainer><Login /></AuthContainer>} />
                        <Route path="/register" element={<AuthContainer><Register /></AuthContainer>} />
                    </Routes>
                </main>
            </div>
        </Router>
    );
}


const PageContainer = ({ children }) => (
    <div className="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8 animate-in fade-in duration-500">
        {children}
    </div>
);


const AuthContainer = ({ children }) => (
    // <div className="flex-grow flex items-center justify-center px-4 py-12">
        // <div className="w-full max-w-md animate-in zoom-in-95 duration-300">
        <div>
            {children}

        </div>
    // {/* </div> */}/
);

export default App;