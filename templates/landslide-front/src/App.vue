<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import FileUpload from './components/FileUpload.vue';
</script>

<template>

<HelloWorld />

  <div class="file-upload-container">
    <FileUpload />
  </div>
</template>

<style scoped>

.file-upload-container { 
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}


</style>
