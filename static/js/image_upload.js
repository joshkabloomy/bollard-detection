document.addEventListener('DOMContentLoaded', function () {
    console.log("before")
    const imageInput = document.getElementById('image-input');
    const imagePreview = document.getElementById('image-preview');

    imageInput.addEventListener('change', function () {
        console.log("inside")
        if (imageInput.files && imageInput.files[0]) {
            const reader = new FileReader();

            reader.onload = function (e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                img.alt = 'Uploaded Image';
                imagePreview.innerHTML = '';
                imagePreview.appendChild(img);
            };

            reader.readAsDataURL(imageInput.files[0]);
            console.log("after")
        }
    });

});

