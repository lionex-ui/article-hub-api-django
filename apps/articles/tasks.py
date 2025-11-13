from celery import shared_task

from apps.articles.models import Article


@shared_task
def analyze_article(article_id: int) -> None:
    article = Article.objects.get(id=article_id)
    article.analysis = {
        "word_count": len(article.content.split()),
        "unique_tags": len(set(article.tags)),
    }
    article.save()
