<script lang="ts">
    import { marked } from 'marked';
    import { fly, fade } from 'svelte/transition';

    let { closeSideMenu, showModal, lightModeEnabled = $bindable() } = $props();

    let clickedButton: string | undefined = $state();

    const faqMarkdown = `
# FAQ

## I don't want to be on this leaderboard!
If your account is ranked here and you don't want it to be, you can just contact me and I'll remove it right away!

## I want to be on this leaderboard!
As long as you have been a LEIC student at FEUP, you're welcome to join!\n
Just contact me and I'll add you to the leaderboard.

## Where do you get student's GitHubs from?
The list of student's GitHub usernames comes from:
- The members of some GitHub organizations created for some classes.
- Public spreadsheets from some classes.
- Manually adding some people.

## How are scores calculated?
Each student's score is calculated according to this formula:\n
\`Score =  Stars × 20 + Commits × 1 + Pull Requests × 3.5 + Repos × 1 + Followers × 1\`

Ties are then broken using stars, prs, commits, followers, repos, and username (lexicographical order) in that order.\n 

The coefficients are somewhat arbitrarily chosen, but the goal is to value high value contributions more.
Improvement suggestions are welcome!

## When are scores updated?
Scores are updated once a week, at 00:00 Sunday UTC, through a GitHub action.\n
You can check when it was last updated in the top right corner.\n
You can also check the status of the last fetch in the [GitHub action page](https://github.com/Mews/leic-gh-leaderboard/actions/workflows/update.yaml).

## Do private contributions count?
Student data is fetched using GitHub's GraphQL api, which *usually* cannot see private repos / contributions.\n
So no, private contributions usually aren't counted, with some exceptions, like if you specifically make them visible.
`;

    const contactMarkdown = `
# Contact

Feel free to reach out to me!\n
You can contact me through any of the following channels.

### Discord
mews75

### Email
ar754456@gmail.com
`;

    const licenseMarkdown = `
# License

\`\`\`
MIT License

Copyright (c) 2026 António Charrão

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
\`\`\`
`;

    const menuItems = [
        {
            "text": "FAQ", "func": () => showModal(marked(faqMarkdown))
        },
        {
            "text": "Contact", "func": () => showModal(marked(contactMarkdown))
        },
        {
            "text": "GitHub", "func": () => window.open("https://github.com/Mews/leic-gh-leaderboard")
        },
        {
            "text": "License", "func": () => showModal(marked(licenseMarkdown))
        },
    ]

    const fetchData = (async () => {
        const response = await fetch('data/fetchdata.json');
        const data = await response.json();
        return data;
    })()

</script>

<button class="backdrop" transition:fade={{duration:200}} onclick={closeSideMenu} aria-label="Close Side Menu"></button>

<aside transition:fly={{ x: -300, duration: 500 }}>
    <nav>
        <h2>Menu</h2>
        <ul>
            <li>
                <label for="light-mode-checkbox" class="switch">
                    <span>Light mode</span>
                    <div class="toggle-container">
                        <input type="checkbox" bind:checked={lightModeEnabled} id="light-mode-checkbox">
                        <span class="slider"></span>
                    </div>
                </label>
                
            </li>

            {#each menuItems as menuItem}
                <li>
                    <button class="text-button"
                    onclick={()=>{
                        clickedButton = menuItem.text;
                        setTimeout(()=>clickedButton = undefined, 200)

                        menuItem.func()
                    }} 
                    class:clicked={clickedButton===menuItem.text}>
                        {menuItem.text}
                    </button>
                </li>
            {/each}
        </ul>

        <span class="user-count-display">
            Currently ranking:<br>
            {#await fetchData}
                Loading...
            {:then fetchData} 
                {fetchData.user_count} students
            {:catch error}
                Couldn't Couldn't student count
            {/await}
        </span>
    </nav>
</aside>

<style>
    .backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(2px);
        z-index: 100;
    }

    aside {
        position: fixed;
        top: 0;
        left: 0;
        width: 20vw;
        height: 100vh;
        background-color: var(--bg-1);
        box-shadow: 5px 0 15px rgba(0, 0, 0, 0.2);
        z-index: 101;
        padding: 2rem;
    }

    h2 {
        font-family: "Space Grotesk", sans-serif;
        font-weight: 500;
        font-style: normal;
        font-size: clamp(1.5rem, 2.5vw, 2rem);

        color: var(--text-2);

        margin-bottom: 4.5rem;
    }
    
    ul {
        list-style-type: none;
        padding: 0;
        padding-left: 0.5rem;
    }

    button.text-button {
        border: none;
        background-color: inherit;

        color: var(--text-1);

        margin-bottom: 2rem;

        transition: all 0.5 ease-in-out;

        font-family: "Raleway", sans-serif;
        font-weight: 600;
        font-size: clamp(1.1rem, 1.5vw, 2rem);

        transition: all 0.5 ease-in-out;
    }

    button.text-button:hover {
        color:var(--accent-1);

        transform: scale(1.1);
    }

    button.text-button.clicked {
        transform: scale(0.95);
        filter: brightness(0.8);
        transition: transform 0.1s;
    }

    .switch {
        display: flex;
        flex-direction: column;
        align-items: start;
        justify-content: space-between;
        width: 100%;
        cursor: pointer;
        margin-bottom: 2rem;
        
        font-family: "Raleway", sans-serif;
        font-weight: 600;
        font-size: clamp(1.1rem, 1.5vw, 2rem);
        color: var(--text-1);
    }

    .switch > span {
        margin-bottom: 1rem;
    }

    .toggle-container {
        position: relative;
        width: 50px;
        height: 26px;
        flex-shrink: 0;
    }

    .toggle-container input {
        opacity: 0;
        width: 0;
        height: 0;
    }

    .slider {
        position: absolute;
        cursor: pointer;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: var(--accent-4);
        transition: .4s;
        border-radius: 34px;
    }

    .slider:before {
        position: absolute;
        content: "";
        height: 20px;
        width: 20px;
        left: 3px;
        bottom: 3px;
        background-color: var(--accent-2);
        transition: .4s;
        border-radius: 50%;
    }

    input:checked + .slider {
        background-color: var(--bg-3);
    }

    input:checked + .slider:before {
        transform: translateX(24px);
        background-color: var(--accent-1);
    }

    span.user-count-display {
        color: var(--text-1);

        font-family: "Raleway", sans-serif;
        font-weight: 600;
        font-size: clamp(0.7rem, 1vw, 1.5rem);

        transition: all 0.5 ease-in-out;

        margin-top: auto;

        position: absolute;
        bottom: 90px;
    }

</style>
