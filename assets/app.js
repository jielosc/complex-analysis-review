
document.addEventListener('DOMContentLoaded', () => {
  const body = document.body;
  const pageKey = body.dataset.page || '';
  document.querySelectorAll('.nav a').forEach(link => {
    const target = link.getAttribute('href');
    if (target === pageKey || target === pageKey + '.html' || target === './' + pageKey + '.html') {
      link.classList.add('active');
    }
  });

  document.querySelectorAll('[data-expand]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('details.fold').forEach(d => d.open = true);
    });
  });

  document.querySelectorAll('[data-collapse]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('details.fold').forEach(d => d.open = false);
    });
  });

  document.querySelectorAll('.flashcard').forEach(card => {
    card.addEventListener('click', () => card.classList.toggle('flipped'));
  });

  document.querySelectorAll('[data-check]').forEach(box => {
    const key = `complex-analysis-check:${box.dataset.check}`;
    box.checked = localStorage.getItem(key) === '1';
    box.addEventListener('change', () => {
      localStorage.setItem(key, box.checked ? '1' : '0');
    });
  });
});
