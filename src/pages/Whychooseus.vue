<template>
  <Layout>
    <About />
    <Why />
  </Layout>
</template>

<script>
import About from "@/components/About.vue"
import Why from "@/components/Why.vue"
export default {
  components:{
    Why,
    About,
  },
  metaInfo: {
    title: 'Why-Choose-Us'
  }
}
</script>

<style>

</style>
