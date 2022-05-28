<template>
  <div class="home mt-2">
    <div class="container">
      <div v-for="question in questions"
              :key="question.uuid"
      >
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <p class="mb-0"> 
              Posted by: <span class="question-author">
                {{ question.author }}</span>
            </p>
            <h4>{{ question.content }}</h4>
            <p class="mb-0">Answers: {{ question.answers_count }}</p>
          </div>
        </div>
      </div>
    </div>
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

  created() {
    this.getQuestion();
  },

  methods: {
    async getQuestion() {
      let endpoint = '/api/v1/questions/';
      try {
        const response = await axios.get(endpoint);
        this.questions = (response.data.results);
      } catch (error) {
        console.error(error.response);
        alert(error.response.statusText);
      }
    }
  }
}
</script>

<style scoped>

  .question-author {
    font-weight: bold;
    color: rgb(244, 103, 103);
  }

</style>