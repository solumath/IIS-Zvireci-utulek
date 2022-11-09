// send post request to server
localAddress = 'http://127.0.0.1:5500';

$( document ).ready(function() {
    console.log( "ready!" );
    
    
    $("#loginForm").submit(function(e) {
        e.preventDefault();
        const login = $("#login").val();
        const password = $("#password").val();
        const formData = {
            login: login,
            password: password
        };
        
        const headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        };
        
        $.ajax({
            type: "POST",
            headers: headers,
            url: localAddress+"/login",
            data: JSON.stringify(formData),
            dataType: "json",
            success: function(data) {
                successModalWindow("Byl jsi úspěšně přihlášen.");
                document.getElementById("password").value = ""
                console.log(JSON.stringify(data));

                // redirect if modal windows is closed
                $('#successModal').on('hidden.bs.modal', function (e) {
                    window.location.href = localAddress+"/index.html";
                });
            },
            crossDomain: true,
            xhrFields: {
                withCredentials: true
            },
            error: function(data) {
                // if data.responseJSON is undefined, then server is not running
                if (data.responseJSON === undefined) {
                    errorModalWindow("Server není dostupný", "Server není dostupný. Zkuste to prosím později.");
                } else {
                    errorModalWindow("Přihlášení se nezdařilo", data.responseJSON.msg);
                }
                
                document.getElementById("password").value = ""
                console.log(JSON.stringify(data))
            }
        });
    });
    
    $("#registerForm").submit(function(e) {
        e.preventDefault();
        const email = $("#registerEmail").val();
        const login = $("#registerLogin").val();
        const password = $("#registerPassword").val();
        const formData = {
            email: email,
            login: login,
            password: password
        };
        
        const headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        };
        
        $.ajax({
            type: "POST",
            headers: headers,
            url: localAddress+"/register",
            data: JSON.stringify(formData),
            dataType: "json",
            success: function(data) {
                successModalWindow("Byl jsi úspěšně registrován.");
                console.log(JSON.stringify(data));

                // redirect if modal windows is closed
                $('#successModal').on('hidden.bs.modal', function (e) {
                    window.location.href = localAddress+"/index.html";
                });
            },
            crossDomain: true,
            xhrFields: {
                withCredentials: true
            },
            error: function(data) {
                // if data.responseJSON is undefined, then server is not running
                if (data.responseJSON === undefined) {
                    errorModalWindow("Server není dostupný", "Server není dostupný. Zkuste to prosím později.");
                } else {
                    errorModalWindow("Přihlášení se nezdařilo", data.responseJSON.msg);
                }
                
                //iterate through form and clear all inputs
                $("#registerForm").find("input").each(function() {
                    $(this).val("");
                });
                
                console.log(JSON.stringify(data))
            }
        });
    });
}); //end of document ready


//button to close modal window
function closeModalWindow(modal) {
    $(modal).modal('hide');
}


// on key press close modal window
$(document).on('keydown', function(e) {
    closeModalWindow('#errorModal');
    closeModalWindow('#successModal');
});


// modal with success message
function successModalWindow(title) {
    const modalWindow = document.createElement('div');
    modalWindow.className = 'modal fade';
    modalWindow.id = 'successModal';
    modalWindow.setAttribute('role', 'dialog');
    modalWindow.setAttribute('aria-labelledby', 'modal-label');
    modalWindow.setAttribute('aria-hidden', 'true');
    modalWindow.innerHTML = `
        <div class="modal-dialog" role="document">
            <div class="modal-content" style="background-color: #6eba5d; --bs-modal-header-border-color: None;">
                <div class="modal-header">
                    <h5 class="modal-title" id="success-title">Title</h5>
                    <button type="button" class="btn btn-close" class="btn-close" aria-label="Close" onclick="closeModalWindow('#successModal')"></button>
                </div>
            </div>
        </div>
    `;

    document.body.appendChild(modalWindow);
    $('#success-title').text(title);
    $('#successModal').modal('show');
}


// modal with error message
function errorModalWindow(title, message) {
    const modalWindow = document.createElement('div');
    modalWindow.className = 'modal fade';
    modalWindow.id = 'errorModal';
    modalWindow.setAttribute('role', 'dialog');
    modalWindow.setAttribute('aria-labelledby', 'modal-label');
    modalWindow.setAttribute('aria-hidden', 'true');
    modalWindow.innerHTML = `
        <div class="modal-dialog" role="document">
            <div class="modal-content" style="background-color: #f26374; --bs-modal-header-border-color: black;">
                <div class="modal-header">
                    <h5 class="modal-title" id="error-title">Title</h5>
                    <button type="button" class="btn btn-close" class="btn-close" aria-label="Close" onclick="closeModalWindow('#errorModal')"></button>
                </div>
                <div class="modal-body">
                    <p id="modal-message">Message</p>
                </div>
            </div>
        </div>
    `;

    document.body.appendChild(modalWindow);
    $('#error-title').text(title);
    $('#modal-message').text(message);
    $('#errorModal').modal('show');
}
