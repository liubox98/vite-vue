<template>
  <div>
    <router-link to="/">Home</router-link>
    <p />
    <router-link to="/about">About</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>