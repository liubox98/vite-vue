<template>
    <div>
        <h1>Index Page</h1>
        <button @click="getData">Fetch Data</button>
        <div v-if="data">{{ data.message }}</div>
    </div>
</template>

<script>

import { fetchData } from '../api';

export default {
    name: 'Index',
    data() {
        return {
            data: null,
        };
    },
    methods: {
        async getData() {
            try {
                const response = await fetchData();
                console.log('response:', response)
                this.data = response.data;
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
    },
};
</script>
