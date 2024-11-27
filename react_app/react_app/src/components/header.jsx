import React from "react";

const Header = () => {
  return (
    <div style={styles.header}>
      FaRon
    </div>
  );
};

const styles = {
  header: {
    display: "flex",
    justifyContent: "center", 
    alignItems: "center",     
    padding: "1rem 0",         
    backgroundColor: "#282c34", 
    color: "#ffffff",         
    fontSize: "2rem",         
    fontWeight: "bold",       
    height: "60px",           
  },
};

export default Header;
