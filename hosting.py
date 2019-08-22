from waitress import serve
import kopomeal
serve(kopomeal.app, host='0.0.0.0', port=80)