<template>
    <div>
      <v-container >
        <p class="pa-5 mt-5 text-h5 font-weight-medium text-uppercase text-center">Ready To Sell</p>
        <div class="d-flex justify-center mb-5">
          <v-btn-toggle v-model="text" tile color="orange accent-3" group>
            <v-btn @click="filterData(all)" value="all">All</v-btn>
            <v-btn @click="filterData(design)" value="left">Store</v-btn>
            <v-btn @click="filterData(website)" value="center">Management</v-btn>
            <v-btn @click="filterData(mobile)" value="right">Apps</v-btn>
          </v-btn-toggle>
        </div>

        <v-row>
          <v-col cols="12" sm="12" md="4" lg="3" v-for="(project, index) in projects" :key="index">
             <v-card class="mx-auto" max-width="344">
              <v-img :src="project.image" height="250px"></v-img>
              <p class="text-h5 text-center font-weight-bold mt-5">{{ project.title }}</p>
              <div class="d-flex justify-center">
                <v-btn color="orange white--text mb-5">View Live</v-btn>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
</template>

<script>
export default {
  metaInfo: {
    
  },
  data(){
    return{
      website:'website',
      design:'design',
      mobile:'mobile',
      all:'all',
      text: 'all',
      icon: 'justify',
      toggle_none: null,
      toggle_one: 0,
      toggle_exclusive: 2,
      toggle_multiple: [0, 1, 2],
      show: false,
      filtered: [],
      projectlist:[
        {"title":"Vuetified", "type":"design", "image":"https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"},
        {"title":"techminate", "type":"website", "image":"https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"},
        {"title":"Amber", "type":"website", "image":"https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"},
        {"title":"Decode", "type":"website", "image":"https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"},
        {"title":"Sunnah", "type":"mobile", "image":"https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"},
        {"title":"Phillips", "type":"mobile", "image":"https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"},
      ]
    }
  },
  created(){
    this.filtered = this.projectlist;
  },
  methods:{
    filterData(type){
      if(type=="all"){
        this.filtered = this.projectlist
      }else{
        this.filtered = this.projectlist.filter( d=> d.type === type)
      }
    }
  },

  computed:{
    projects: function(){
      return this.filtered;
    }
  },

}
</script>

<style>

</style>
