import { mount } from 'svelte'
import './lib/style/colors.css'
import './lib/style/fonts.css'
import App from './App.svelte'

const app = mount(App, {
  target: document.getElementById('app')!,
})

export default app
