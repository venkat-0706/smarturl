import { useState } from "react";
import "./App.css";

function App() {

  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);
  const [error, setError] = useState("");

  const shortenURL = async (e) => {

    e.preventDefault();

    if (!url.trim()) {
      setError("Please enter a URL");
      return;
    }

    setLoading(true);
    setError("");
    setShortUrl("");
    setCopied(false);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/api/shorten/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            original_url: url,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setError(
          data.original_url?.[0] ||
          "Unable to shorten this URL"
        );
        return;
      }

      setShortUrl(data.short_url);

    } catch (error) {

      setError(
        "Unable to connect to the server. Please try again."
      );

    } finally {

      setLoading(false);

    }
  };


  const copyURL = async () => {

    try {

      await navigator.clipboard.writeText(shortUrl);

      setCopied(true);

      setTimeout(() => {
        setCopied(false);
      }, 2000);

    } catch (error) {

      console.log(error);

    }
  };


  return (
    <div className="app">

      {/* NAVBAR */}

      <nav className="navbar">

        <div className="nav-container">

          <div className="logo">
            Smart<span>URL</span>
          </div>

          <div className="nav-links">

            <a href="#home">Home</a>

            <a href="#features">Features</a>

            <a href="#about">About</a>

            <button className="login-btn">
              Login
            </button>

            <button className="register-btn">
              Get Started
            </button>

          </div>

        </div>

      </nav>


      {/* HERO */}

      <main id="home">

        <section className="hero-section">

          <div className="hero-content">

            <div className="badge">
              <span className="status-dot"></span>
              Fast & Secure URL Shortener
            </div>


            <h1>
              Turn long URLs into
              <span> powerful links.</span>
            </h1>


            <p className="hero-description">
              Create short, memorable and shareable links
              in seconds. Track your links and simplify
              the way you share URLs.
            </p>


            {/* URL FORM */}

            <form
              className="url-form"
              onSubmit={shortenURL}
            >

              <div className="input-wrapper">

                <span className="input-icon">
                  🔗
                </span>

                <input
                  type="url"
                  placeholder="Paste your long URL here..."
                  value={url}
                  onChange={(e) =>
                    setUrl(e.target.value)
                  }
                />

              </div>


              <button
                type="submit"
                className="shorten-btn"
                disabled={loading}
              >

                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Shortening...
                  </>
                ) : (
                  <>
                    Shorten URL
                    <span>→</span>
                  </>
                )}

              </button>

            </form>


            {/* ERROR */}

            {error && (
              <div className="error-message">
                ⚠ {error}
              </div>
            )}


            {/* RESULT */}

            {shortUrl && (

              <div className="result-card">

                <div className="result-icon">
                  ✓
                </div>

                <div className="result-content">

                  <span>Your shortened URL</span>

                  <a
                    href={shortUrl}
                    target="_blank"
                    rel="noreferrer"
                  >
                    {shortUrl}
                  </a>

                </div>

                <button
                  className="copy-btn"
                  onClick={copyURL}
                >
                  {copied ? "Copied ✓" : "Copy"}
                </button>

              </div>

            )}


            <div className="trust-text">
              🔒 Free to use&nbsp;&nbsp; • &nbsp;&nbsp;⚡ Lightning fast&nbsp;&nbsp; • &nbsp;&nbsp;🛡 Secure
            </div>

          </div>


          {/* DECORATIVE ELEMENTS */}

          <div className="floating-card card-one">
            <span>🔗</span>
            <div>
              <strong>Short URL</strong>
              <small>smrt.url/Ab12X</small>
            </div>
          </div>


          <div className="floating-card card-two">
            <span className="green-check">✓</span>
            <div>
              <strong>Link Created</strong>
              <small>Just now</small>
            </div>
          </div>


          <div className="gradient-circle circle-one"></div>
          <div className="gradient-circle circle-two"></div>

        </section>


        {/* FEATURES */}

        <section
          id="features"
          className="features-section"
        >

          <div className="section-heading">

            <span>POWERFUL FEATURES</span>

            <h2>
              Everything you need for
              <br />
              better links.
            </h2>

            <p>
              Simple on the surface. Powerful underneath.
            </p>

          </div>


          <div className="features-grid">

            <div className="feature-card">

              <div className="feature-icon purple">
                ⚡
              </div>

              <h3>Lightning Fast</h3>

              <p>
                Generate short URLs instantly with
                our optimized backend.
              </p>

            </div>


            <div className="feature-card">

              <div className="feature-icon blue">
                📊
              </div>

              <h3>Track Analytics</h3>

              <p>
                Monitor clicks and understand how
                your links are performing.
              </p>

            </div>


            <div className="feature-card">

              <div className="feature-icon green">
                🔒
              </div>

              <h3>Secure Links</h3>

              <p>
                Your URLs are protected and managed
                securely.
              </p>

            </div>

          </div>

        </section>


        {/* CTA */}

        <section className="cta-section">

          <div className="cta-content">

            <h2>
              Ready to simplify your links?
            </h2>

            <p>
              Create your first short URL today.
            </p>

            <button
              className="cta-btn"
              onClick={() =>
                window.scrollTo({
                  top: 0,
                  behavior: "smooth",
                })
              }
            >
              Shorten a URL →
            </button>

          </div>

        </section>

      </main>


      {/* FOOTER */}

      <footer>

        <div className="footer-container">

          <div className="logo">
            Smart<span>URL</span>
          </div>

          <p>
            © 2026 SmartURL. Built with Django &
            React.
          </p>

          <div className="footer-links">
            <a href="#home">Home</a>
            <a href="#features">Features</a>
            <a href="#about">About</a>
          </div>

        </div>

      </footer>

    </div>
  );
}

export default App;