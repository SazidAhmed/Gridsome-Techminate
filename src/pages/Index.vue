<template>
  <Layout>
    <Home />
    <About />
    <Workflow />
    <Why />
    <Service/>
  </Layout>
</template>

<script>
import Home from "@/components/Home.vue"
import About from "@/components/About.vue"
import Why from "@/components/Why.vue"
import Service from "@/components/Service.vue"
import Workflow from "@/components/Workflow.vue"

export default {
  components:{
    Home,
    About,
    Service,
    Why,
    Workflow,
  },
  metaInfo: {
    title: 'Home'
  }
}
</script>

<style scoped>
.bg{
  background: linear-gradient(90deg, #FC575E 0%, #F7B42C 100%), #C4C4C4;
  border-radius: 0px 0px 300px 300px;
}

</style>
