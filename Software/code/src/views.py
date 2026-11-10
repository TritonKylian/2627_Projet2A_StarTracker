# views.py (Django)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from redis import Redis
from rq import Queue
import json

# Connexion à la file d'attente Redis
redis_conn = Redis(host='localhost', port=6379)
q = Queue(connection=redis_conn)

@csrf_exempt # Attention, ajoutez les vérifications CSRF en production
def api_goto_target(request):
    """
    Accepte les actions stop, align et goto via la même API.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action', 'goto')

            if action == 'stop':
                job = q.enqueue('worker.stop_mount_tracking')
                message = "Arrêt du suivi demandé. Attendez la fin de la tâche avant de déplacer la monture."
            elif action == 'align':
                reference = data.get('reference')
                if not isinstance(reference, str) or not reference.strip():
                    return JsonResponse(
                        {"status": "error", "message": "Le nom de l'astre de référence est requis."},
                        status=400,
                    )
                job = q.enqueue('worker.align_mount_to_target', reference.strip())
                message = (
                    f"Enregistrement de l'alignement sur {reference.strip()} demandé. "
                    "Après l'arrêt du suivi, centrez cet astre puis envoyez cette action."
                )
            elif action == 'goto':
                target = data.get('target')
                if not isinstance(target, str) or not target.strip():
                    return JsonResponse(
                        {"status": "error", "message": "Le nom de la cible est requis."},
                        status=400,
                    )
                job = q.enqueue('worker.move_mount_to_target', target.strip())
                message = f"Ordre envoyé. Mouvement vers {target.strip()} en cours..."
            else:
                return JsonResponse(
                    {"status": "error", "message": "Action invalide ; utilisez stop, align ou goto."},
                    status=400,
                )

            return JsonResponse({
                "status": "success",
                "message": message,
                "job_id": job.id
            })

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    
    return JsonResponse({"status": "error", "message": "Méthode non autorisée"}, status=405)