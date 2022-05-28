<template>
    <div v-if="question" class="container">
      <h1>{{ question.content }}</h1>
      <p class="mb-0">
        Posted by:
        <span class="author-name">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
    </div>
    <div v-else>
        <h1 class="error text-center">404 - Question Not Found</h1>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js'

export default {
    name: "QuestionDetail",

    props: {
        slug: {
            type: String,
            required: true,
        }
    },

    data() {
        return {
            question: null,
        }
    },

    methods: {
        setPageTitle(title) {
            document.title = title;
        },

        async getQuestionDetail() {
            const endpoint = `/api/v1/questions/${this.slug}/`;
            try {
                const response = await axios.get(endpoint);
                this.question = response.data;

            } catch(error) {
                console.error(error.response);
            }
        }
    },

    created() {
        this.getQuestionDetail()
    }
}
</script>

<style>
    .author-name {
        font-weight: bold;
          color: #dc3545; 
    }
</style>
