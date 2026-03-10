<script lang="ts">
    import { fly, fade } from 'svelte/transition';

    let { closeSideMenu } = $props();

    let clickedButton: string | undefined = $state();

    const menuItems = [
        {
            "text": "FAQ", "func": () => alert("lol")
        },
        {
            "text": "Credits", "func": () => alert("lol")
        },
        {
            "text": "About", "func": () => alert("lol")
        },
        {
            "text": "GitHub", "func": () => window.open("https://github.com/Mews/leic-gh-leaderboard")
        },
        {
            "text": "License", "func": () => alert("lol")
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
        padding: none;
        padding-left: 0.5rem;
    }

    button.text-button {
        border: none;
        background-color: inherit;

        color: var(--text-1);

        margin-bottom: 2rem;

        font-family: "Raleway", sans-serif;
        font-weight: 600;
        font-size: clamp(1rem, 1.5vw, 2rem);

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
