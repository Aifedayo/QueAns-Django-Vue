<template>
  <div class="home">
    <h1>Homepage</h1>
    <button @click="getQuestion">Load Questions</button>
  </div>
</template>

<script>
// @ is an alias to /src
import { axios } from "@/common/api.service.js";
export default {
  name: "HomeView",

  data() {
    return {
      questions: []
    }
  },

  methods: {
    async getQuestion() {
      let endpoint = '/api/v1/questions/';
      try {
        const response = await axios.get(endpoint);
        console.log(response)
      } catch (error) {
        console.error(error.response);
        alert(error.response.statusText);
      }
    }
  }
}
</script>
