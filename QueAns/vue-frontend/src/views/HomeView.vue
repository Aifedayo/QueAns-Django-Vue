<template>
  <div class="home mt-5">
    <div class="container">
      <div v-for="category in categories"
              :key="category.pk"
      >
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <router-link :to="{ name: 'question-list', params: {slug: category.slug} }"
              class="question-link"
            >
              <p class="mb-0"> 
                <span class="question-author">
                {{ category.name }}</span>
              </p>
            </router-link>
          </div>
        </div>
      </div>

      <div class="my-4">
        <p v-show="loadingCategories">...loading...</p>
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
      categories: [],
      next: null,
      loadingCategories: false,
    }
  },

  created() {
    this.getQuestions();
  },

  methods: {
    async getQuestions() {
      let endpoint = '/api/v1/categories/';
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingCategories = true;
      try {
        const response = await axios.get(endpoint);
        console.log(response);
        this.categories.push(...response.data.results);
        this.loadingCategories = false;
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