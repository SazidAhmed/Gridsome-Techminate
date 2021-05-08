<template>
    <div>
      <v-container >
        <p class="pa-5 mt-10 text-h3 font-weight-medium text-uppercase text-center">Completed Projects</p>
        <v-row>
          <v-col cols="12" sm="12" md="4" v-for="(service, index) in services" :key="index">
             <v-card class="mx-auto" max-width="344">
              <v-img :src="service.image" height="250px"></v-img>
              <p class="text-h5 text-center font-weight-bold mt-5">{{ service.title }}</p>
              <div class="d-flex justify-center">
                <v-btn color="blue white--text mb-5">View Live</v-btn>
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
      show: false,
      services:[
        {"title":"Online Store","image":"https://cdn.vuetifyjs.com/images/cards/sunshine.jpg", "color":"blue--text", "number":"01", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"Website Development","icon":"mdi-web", "color":"purple--text", "number":"02", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"UI/UX Design","icon":"mdi-material-design", "color":"red--text", "number":"03", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"Cloud & DevOps","icon":"mdi-cloud-tags", "color":"green--text", "number":"04", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"Analytic Solutions","icon":"mdi-chart-bar-stacked", "color":"orange--text", "number":"05", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"Database Administration","icon":"mdi-microsoft-access", "color":"teal--text", "number":"06", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"}
      ]
    }
  }
}
</script>

<style>

</style>
