<template>
    <div>
      <v-container >
        <p class="pa-5 mt-10 text-h3 font-weight-medium text-uppercase text-center">Get Ready Software</p>
        <v-row>
          <v-col cols="12" sm="12" md="4" v-for="(service, index) in services" :key="index">
            <v-card width="400" class="rounded-xl mx-auto">
                <div class="d-flex justify-space-around pt-10">
                    <span class="ml-5 d-inline">
                        <v-icon size="100" :class="service.color" class="text--lighten-1">{{ service.icon }}</v-icon>
                    </span>
                    <p class="mr-5 grey--text text--lighten-4 text-h1 font-weight-bold d-inline">{{ service.number }}</p>
                </div>
                <p class="text-h5 text-center font-weight-bold mt-5">{{ service.title }}</p>
                <p class="font-weight-medium ml-10 mr-10 pb-8">
                  {{ service.description }}
                </p>
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
      services:[
        {"title":"Software Development","icon":"mdi-view-dashboard", "color":"blue--text", "number":"01", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
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
