<template>
  <UploadFile filetype="equities"></UploadFile>
  <br>
  <UploadFile filetype="returns"></UploadFile>
  <div class="container">
    <LineChart ></LineChart>
  </div>
  
</template>

<script>
import UploadFile from './components/UploadFile.vue';
import LineChart from './components/LineChart.vue';
export default {
  name: 'App',
  components: {
    UploadFile,
    LineChart
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.container{
  width: 50%;
  height: 50%;
}
</style>
