// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api/

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin');
const axios = require('axios')

module.exports = function (api) {
  // api.loadSource(({ addCollection }) => {
    
  // })
  api.loadSource(async actions => {
    const { data } = await axios.get('http://127.0.0.1:8000/api/projects')

    const collection = actions.addCollection('Projects')

    for (const project of data) {
      collection.addNode({
        id: project.id,
        title: project.title,
        link: project.link,
        project_type: project.project_type,
        get_image: project.get_image
      })
    }
  })

  api.createPages(({ createPage }) => {
    // Use the Pages API here: https://gridsome.org/docs/pages-api/
  })

  api.chainWebpack((config, { isServer }) => {
    config.plugin('vuetify-loader').use(VuetifyLoaderPlugin);
  });

  api.loadSource(actions => {
    // Use Data Store API here
  });
}
