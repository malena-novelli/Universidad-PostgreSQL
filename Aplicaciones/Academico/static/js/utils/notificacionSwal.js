const notificacionSwal=(titleText, text, icon, confirmButtonText)=>{
    Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon, //warning, error, succes, info
        confirmButtonText: confirmButtonText
    });
};
