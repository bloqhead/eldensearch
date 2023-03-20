import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// Font Awesome library
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// Font Awesome icons
import {
  faBookBible, // holy
  faBrain, // intelligence
  faFire, // fire
  faLightbulb, // light
  faPersonRunning, // dexterity
  faSkull,
  faSword, // strength
  faSwords,
  faWandMagicSparkles, // magic
  faWeightHanging, // weight
} from '@fortawesome/sharp-regular-svg-icons'

/* add icons to the library */
library.add(
  faBookBible,
  faBrain,
  faFire,
  faLightbulb,
  faPersonRunning,
  faSkull,
  faSword,
  faSwords,
  faWandMagicSparkles,
  faWeightHanging,
)

createApp(App)
  .component('fa', FontAwesomeIcon)
  .mount('#app')
