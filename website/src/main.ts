import { mount } from 'svelte'
import './lib/colors.css'
import './lib/fonts.css'
import App from './App.svelte'

const app = mount(App, {
  target: document.getElementById('app')!,
})

export default app
