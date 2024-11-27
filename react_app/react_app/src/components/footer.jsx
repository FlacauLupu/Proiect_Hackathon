import React from "react";

const Footer = () => {
    return (
        <div style={styles.footer}>
            <button style={styles.button}>Log In</button>
            <button style={styles.iconButton}>
                <img
                    src="https://cdn-icons-png.flaticon.com/512/1828/1828817.png" 
                    alt="Add User Icon"
                    style={styles.icon}
                />
            </button>
        </div>
    );
};

const styles = {
    footer: {
        display: "flex",
        justifyContent: "center",
        gap: "10px",
        padding: "10px",
    },
    button: {
        padding: "10px 20px",
        backgroundColor: "#007bff",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
        fontSize: "16px",
    },
    iconButton: {
        padding: "10px",
        backgroundColor: "#28a745",
        border: "none",
        borderRadius: "50%", 
        cursor: "pointer",
    },
    icon: {
        width: "20px",
        height: "20px",
    },
};

export default Footer;
