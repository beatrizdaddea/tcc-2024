<template>
  <div class="sidebar">
    <div class="sidebar-header">Menu</div>
    <ul>
      <li @click="selectedOption = 'about'">Sobre Nós</li>
      <li @click="selectedOption = 'documentation'">Documentação</li>
      <li @click="selectedOption = 'info'">Informações</li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const selectedOption = ref<string>('about');
</script>

<style scoped>
.sidebar {
  width: 250px;
  background-color: #333;
  color: white;
  padding: 20px;
}

.sidebar-header {
  font-size: 20px;
  margin-bottom: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  cursor: pointer;
  padding: 10px;
}

li:hover {
  background-color: #555;
}

.content {
  margin-left: 270px;
  /* Tamanho da barra lateral + margem */
  padding: 20px;
}
</style>
