const filters = [...document.querySelectorAll('[data-filter]')];
const projects = [...document.querySelectorAll('[data-category]')];
for (const button of filters) button.addEventListener('click', () => {
  for (const other of filters) other.setAttribute('aria-pressed', String(other === button));
  let count = 0;
  for (const project of projects) {
    project.hidden = button.dataset.filter !== 'all' && project.dataset.category !== button.dataset.filter;
    if (!project.hidden) count++;
  }
  document.querySelector('#project-count').textContent = String(count);
});
const motion = document.querySelector('.motion');
motion.addEventListener('click', () => {
  const scene = document.querySelector('machine-scene');
  const paused = !scene.hasAttribute('paused');
  scene.toggleAttribute('paused', paused);
  motion.textContent = paused ? '▷' : 'Ⅱ';
  motion.setAttribute('aria-label', paused ? motion.dataset.play : motion.dataset.pause);
});
