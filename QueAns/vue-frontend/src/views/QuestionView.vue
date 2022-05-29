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
            <router-link :to="{ name: 'question', params: {slug: question.slug} }"
              class="question-link"
            >
              <h4>{{ question.content }}</h4>
            </router-link>
            <p class="mb-0">Answers: {{ question.answers_count }}</p>
          </div>
        </div>
      </div>

      <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
        <button v-show="next" @click="getQuestions"
              class="btn btn-sm btn-outline-danger"
        >
          Load more questions
        </button>
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
      questions: [],
      next: null,
      loadingQuestions: false,
    }
  },

  created() {
    this.getQuestions();
  },

  methods: {
    async getQuestions() {
      let endpoint = '/api/v1/questions/';
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      try {
        const response = await axios.get(endpoint);
        this.questions.push(...response.data.results);
        this.loadingQuestions = false;
        if (response.data.next){
          this.next = response.data.next;
        } else {
          this.next = null;
        }
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

  .question-link {
    text-decoration: none;
    color: black;
    font-weight: 400;
  }

  .question-link:hover {
    text-decoration: none;
    color: rgb(63, 61, 61);
    font-weight: 400;
  }

</style>