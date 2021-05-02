<template>
    <v-container>
        <v-row class="">
            <v-col cols="12" sm="12" md="8" lg="5">
                <div class="text-uppercase">
                    <p class="font-weight-medium text-h5 mt-10">We Create Result-Oriented Dynamic Applications</p>
                    <p class="mt-5">Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis itaque, perspiciatis fugiat natus libero perferendis et ipsa debitis sint laborum vero quo dignissimos doloremque labore molestiae similique soluta enim iusto mollitia accusamus! Accusantium a ab iusto, amet in dicta aperiam id voluptatibus quisquam minima doloribus quod delectus aspernatur tenetur nemo.</p>
                </div>
                <div class="mt-10">
                    <v-list two-line color="orange lighten-5">
                        <template v-for="(item, index) in data">
                            <v-list-item :key="index" >
                                <v-list-item-avatar size="60">
                                    <v-icon size="50" :color="item.color">{{ item.icon }}</v-icon>
                                </v-list-item-avatar>
                                <v-list-item-content>
                                    <v-list-item-title v-html="item.title" class="font-weight-medium"></v-list-item-title>
                                    <v-list-item-subtitle v-html="item.description"></v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                        </template>
                    </v-list>
                </div>
            </v-col>
            <v-col cols="12" sm="12" md="4" lg="6">
                <div class="text-center">
                    <span class="">
                        <g-image class="mt-5" src="~/assets/why/why.png" quality="90" width="600" height="392" fit="fill"/>
                    </span>
                </div>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
  metaInfo: {
    
  },
  data(){
    return{
      data:[
        {"title":"First Growing Proccess","color":"blue", "icon":"mdi-state-machine", "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit."},
        {"title":"Clean Code","color":"purple", "icon":"mdi-console", "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit."},
        {"title":"Well Documentation","color":"red", "icon":"mdi-file-document-multiple-outline", "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit."},
      ]
    }
  }
}
</script>

<style scoped>

</style>
