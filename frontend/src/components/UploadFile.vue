


<template>

<label for="">{{filetype}}</label>
<input type="file" @change="onFileSelected">
<button @click="onUpload">Upload</button>



</template>

<script>
    import axios from 'axios';
    export default {
    name: "UploadFile",
    props: ["filetype"],
    methods: {
        onFileSelected(event) {
            this.selectedFile = event.target.files[0];
        },
        onUpload() {
            const fd = new FormData();
            fd.append("file", this.selectedFile);
            fd.append("filetype", this.filetype);
            axios.post("http://localhost:8000/csv", fd)
                .then(res => {
                console.log(res);
            });
        }
    },
}
</script>