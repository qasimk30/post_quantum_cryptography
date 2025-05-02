// Main JavaScript file for PQCrypto Web App

// Function to show notifications
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show notification-toast`;
    notification.role = 'alert';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    // Add custom styling
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '1050';
    notification.style.minWidth = '300px';
    
    // Add to document
    document.body.appendChild(notification);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 150);
    }, 5000);
}

// Copy text to clipboard function
function copyToClipboard(text) {
    if (!navigator.clipboard) {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        textArea.style.top = '-999999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        
        try {
            const successful = document.execCommand('copy');
            document.body.removeChild(textArea);
            return successful;
        } catch (err) {
            document.body.removeChild(textArea);
            return false;
        }
    }
    
    return navigator.clipboard.writeText(text)
        .then(() => true)
        .catch(() => false);
}

// Add copy button to all readonly textareas
document.addEventListener('DOMContentLoaded', function() {
    const readonlyTextareas = document.querySelectorAll('textarea[readonly]');
    
    readonlyTextareas.forEach(textarea => {
        // Create container for textarea and button
        const container = document.createElement('div');
        container.className = 'position-relative';
        
        // Get the parent element of the textarea
        const parent = textarea.parentNode;
        
        // Replace the textarea with the container
        parent.replaceChild(container, textarea);
        
        // Add the textarea to the container
        container.appendChild(textarea);
        
        // Create the copy button
        const copyButton = document.createElement('button');
        copyButton.className = 'btn btn-sm btn-outline-secondary position-absolute';
        copyButton.style.right = '5px';
        copyButton.style.top = '5px';
        copyButton.innerHTML = '<i class="bi bi-clipboard"></i> Copy';
        copyButton.addEventListener('click', function() {
            const success = copyToClipboard(textarea.value);
            if (success) {
                showNotification('Copied to clipboard', 'success');
            } else {
                showNotification('Failed to copy to clipboard', 'danger');
            }
        });
        
        // Add the button to the container
        container.appendChild(copyButton);
    });
});

// Add animation effects for algorithm cards on homepage
document.addEventListener('DOMContentLoaded', function() {
    const algoCards = document.querySelectorAll('.card');
    
    algoCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.2)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });
});