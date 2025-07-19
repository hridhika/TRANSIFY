// hackathon/static/js/main.js

console.log("Transify main.js loaded!");

// --- Phantom Wallet Detection and Connection ---
// This script checks if Phantom wallet is installed and provides a way to connect.
// It's a basic example, full integration would involve more error handling and state management.

const phantomConnectButton = document.getElementById('phantom-connect-button');
const phantomStatusDiv = document.getElementById('phantom-status');

if (phantomConnectButton && phantomStatusDiv) {
    // Function to update the UI based on Phantom's connection status
    const updatePhantomStatus = () => {
        if ("solana" in window && window.solana.isPhantom) {
            phantomStatusDiv.textContent = "Phantom Wallet Detected!";
            phantomConnectButton.style.display = 'block'; // Show button if detected
            if (window.solana.isConnected) {
                phantomStatusDiv.textContent = `Phantom Wallet Connected: ${window.solana.publicKey.toBase58()}`;
                phantomConnectButton.textContent = "Disconnect Phantom";
                // You can fetch token balance here if needed, after connection
            } else {
                phantomConnectButton.textContent = "Connect Phantom Wallet";
            }
        } else {
            phantomStatusDiv.textContent = "Phantom Wallet Not Found. Please install it.";
            phantomConnectButton.style.display = 'none'; // Hide button if not detected
        }
    };

    // Event listener for the connect/disconnect button
    phantomConnectButton.addEventListener('click', async () => {
        if ("solana" in window && window.solana.isPhantom) {
            try {
                if (window.solana.isConnected) {
                    // Disconnect logic
                    await window.solana.disconnect();
                    console.log("Phantom disconnected.");
                    phantomStatusDiv.textContent = "Phantom Wallet Disconnected.";
                    phantomConnectButton.textContent = "Connect Phantom Wallet";
                } else {
                    // Connect logic
                    await window.solana.connect();
                    console.log("Phantom connected. Public Key:", window.solana.publicKey.toBase58());
                    phantomStatusDiv.textContent = `Phantom Wallet Connected: ${window.solana.publicKey.toBase58()}`;
                    phantomConnectButton.textContent = "Disconnect Phantom";
                    // In a real app, you'd send this publicKey to your backend for registration/verification
                }
            } catch (error) {
                console.error("Phantom connection/disconnection error:", error);
                phantomStatusDiv.textContent = `Error: ${error.message || "Could not connect to Phantom."}`;
            }
        } else {
            alert("Phantom Wallet is not installed. Please install it from phantom.app");
            window.open("https://phantom.app/", "_blank");
        }
    });

    // Initial check and update status
    updatePhantomStatus();

    // Listen for Phantom connection/disconnection events
    window.solana?.on("connect", updatePhantomStatus);
    window.solana?.on("disconnect", updatePhantomStatus);

} else {
    console.warn("Phantom connect button or status div not found. Skipping Phantom integration setup.");
}

// --- End Phantom Wallet Integration ---