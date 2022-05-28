<template>
    <div class="container my-2">
        <h1 class="mb-3">
            Ask a Question
        </h1>
        <form @submit.prevent="onSubmit">
            <textarea
                v-model="questionBody"
                class="form-control"
                placeholder="What do you have in mind?"
                rows="5">
            </textarea>
            <button  class="btn btn-success mt-3" type="submit">Ask your Question</button>
        </form>
        <p v-if="error" class="nuted mt-2">
            {{ error }}
        </p>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js'
export default {
    name: "QuestionEditor",

    data() {
        return {
            questionBody: null,
            error: null,
        }
    },

    methods: {
        async performNetworkRequest() {
            let endpoint = "/api/v1/questions/";
            let method = "POST";
            try {
                const response = await axios({
                    method: method,
                    url: endpoint,
                    data: {content: this.questionBody}
                })
                this.$router.push({name: 'question', params: { slug: response.data.slug }})
            } catch (error) {
                console.error(error.response);
                alert(error.response.statusText);
            }
        },

        onSubmit() {
            if (!this.questionBody) {
                this.error = "The question body cannot be empty"
            } else if (this.questionBody.length > 255) {
                this.error = "The length of the question should not be greater than 255"
            } else {
                this.performNetworkRequest();
            }
        }
    }
}
</script>