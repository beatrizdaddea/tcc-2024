<template>
  <div class="container">
    <label for="fileInput" class="file-label">Enviar arquivo</label>
    <input type="file" @change="handleFileUpload" id="fileInput" class="file-input" />
    <div class="spacer"></div>
  </div>

  <div v-if="fileUrl" class="image-container">
    <p> Imagem Original:</p>
    <div class="original-image">
      <img :src="fileUrl" alt="Imagem selecionada" />
      <button @click="closeImage">Fechar</button>
    </div>
  </div>

  <div v-if="detectedFileName" class="detected-file">
    <p>Arquivo detectado: {{ detectedFileName }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const file = ref<File | null>(null);
const fileUrl = ref<string | null>(null);
const detectedFileName = ref<string | null>(null);

const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    file.value = target.files[0];
    fileUrl.value = URL.createObjectURL(target.files[0]);
    uploadOriginalImage();
  }
};

const closeImage = () => {
  fileUrl.value = null;
};

const uploadOriginalImage = async () => {
  if (file.value) {
    const formData = new FormData();
    formData.append('file', file.value);

    try {
      const response = await axios.post('/predict_img', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      if (response.data && response.data.filename) {
        detectedFileName.value = response.data.filename;
      }
    } catch (error) {
      console.error('Erro ao fazer upload da imagem:', error);
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 10px;
  width: 500px;
  height: 25vh;
}

.file-label {
  padding: 20px 10px;
  width: 200px;
  background-color: #333;
  color: #fff;
  text-transform: uppercase;
  text-align: center;
  display: block;
  cursor: pointer;
}

.file-input {
  display: none;
}

.spacer {
  height: 20px; /* Espaçamento de 20px */
}

.image-container {
  margin: 50px 20px;
}

.original-image {
  display: flex;
  align-items: center;
}

.original-image img {
  max-width: 100%;
}

.original-image button {
  margin-left: 10px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #0056b3;
}

@media (min-width: 768px) {
  .container {
    max-width: 400px;
    margin: 0 auto;
  }
}
</style>
