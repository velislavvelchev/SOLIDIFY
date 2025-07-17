document.addEventListener('DOMContentLoaded', function () {
    // Home page
    const homeText = document.getElementById('dynamic-text');
    if (homeText) {
        const message = "Solidify is an application that serves to optimize our habits and align them to our personal goals, so that we can both enjoy our lives while also achieving our goals.\nMost people nowadays, especially in urban cities, have extremely fast and busy lives, where they try to constantly keep up with their numerous aspirations related to things like career paths, physical fitness, personal relationships etc. This very often leads to redundant stress, especially when any of the above-mentioned domains is compromised.";
        typeWriterEffect('dynamic-text', message);
    }

    // Dopamine page
    const dopamineText = document.getElementById('dynamic-text-dopamine');
    if (dopamineText) {
        const dopamineMessage = "Dopamine is a natural brain chemical that acts as a messenger, helping different parts of your brain communicate.\n\nIt's strongly linked to feelings of motivation, satisfaction, and pleasure. While often called the “feel good” chemical, dopamine is really about drive and wanting to achieve things.\n\nWhen you do something rewarding, like eating tasty food or achieving a goal, your brain releases dopamine, encouraging you to repeat those actions. This process is central to how habits form.\n\nIn short: Dopamine motivates you to seek out rewards and build habits. It’s your brain’s way of helping you grow and achieve what matters to you.";
        typeWriterEffect('dynamic-text-dopamine', dopamineMessage);

        // Fade in the video after a delay (can also make this function reusable)
        setTimeout(function() {
            const videoContainer = document.getElementById('dopamine-video-container');
            if (videoContainer) {
                videoContainer.classList.add('visible');
            }
        }, 10000); // 10s delay
    }
});
