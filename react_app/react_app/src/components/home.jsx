import React from "react";
import Header from "./header";
import Footer from "./footer";

const users = {
  id: 1,
  name: "Lupu",
};

const Home = () => {
  return (
    <div style={styles.container}>
      <Header />
      <main style={styles.main}>
        <h1 style={styles.heading}>Welcome, {users.name}</h1>
        <p style={styles.paragraph}>This is the main content area.</p>
      </main>
      <Footer />
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    minHeight: "100vh",
    backgroundColor: "#f5f5f5",
  },
  main: {
    flex: "1", 
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    textAlign: "center",
  },
  heading: {
    fontSize: "2.5rem",
    color: "#333",
    marginBottom: "1rem",
  },
  paragraph: {
    fontSize: "1rem",
    color: "#666",
  },
};

export default Home;
