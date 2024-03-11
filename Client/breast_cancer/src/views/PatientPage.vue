<template>
    <h1>Hi this is patient page</h1>
    <div>
        {{ this.response }}
    </div>
</template>

<script>
    import Services from '../services/services';

    export default {
        data() {
            const data = {
                age: "60-69",
                menopause: "ge40",
                tumor_size: "35-39",
                inv_nodes: "6-8",
                node_caps: "no",
                deg_malig: 3,
                breast: "left",
                breast_quad: "left_up",
                irradiat: "yes"
            }

            return {
                data,
                response: {},
            }
        },

        methods: {
            async post_input() {
                try {
                    const predict = await Services.bc_predict(this.data);
                    if (predict) {
                        this.response = predict;
                    } else {
                        this.response = {error: 'Error'};
                    }
                } catch (err){
                    console.log(err)
                }
            }
        },

        created() {
            this.post_input();
        }
    }
</script>