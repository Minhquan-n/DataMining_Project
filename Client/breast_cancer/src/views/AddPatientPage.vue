<script>
    import services from '@/services/services';

    export default {
        data () {
            return {
                patient: {},
            }
        },

        methods: {
            async create_patient(data) {
                try {
                    const response = await services.create_patient(data);
                    console.log(response)
                } catch (err) {
                    console.log(err)
                }
            }
        }
    }
</script>

<template>
    <h1>hellp</h1>
</template>