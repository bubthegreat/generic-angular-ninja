from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404  # type: ignore
from typing import List, Any
from ninja.orm import create_schema
from ninja import Router

def _get_model_router(model, name):

    router = Router(tags=[name])

    ModelPost = create_schema(model = model, name = f"{name.title()}Post", exclude=['id'])
    ModelGet = create_schema(model = model, name = f"{name.title()}Get")

    @router.post(f"/{name}")
    async def create_instance(request, payload: ModelPost):
        """Create a new instance based on input."""
        instance = await sync_to_async(model.objects.create)(**payload.dict())
        return ModelGet.from_orm(instance)

    @router.post(f"/{name}2")
    async def create_instance2(request, payload: ModelPost):
        """Create a new instance based on input."""
        orm_instnace = await sync_to_async(payload.orm.apply)(ModelPost())
        orm_instnace.save()
        return ModelGet.from_orm(orm_instnace)

    @router.get(f"/{name}/" + "{model_id}", response=ModelGet)
    async def get_instance(request, model_id: int):
        """Return an instance for the ID specified."""
        instance = await sync_to_async(get_object_or_404)(model, id=model_id)
        return ModelGet.from_orm(instance)

    @router.get(f"/{name}", response=List[ModelGet])
    async def list_instances(request):
        """Return a list of all model instances."""
        qs = await sync_to_async(list)(model.objects.all())
        return qs

    @router.put(f"/{name}/" + "{model_id}")
    async def update_instance(request, model_id: int, payload: ModelPost):
        """Update the model instance with the payload."""
        instance = await sync_to_async(get_object_or_404)(model, id=model_id)
        for attr, value in payload.dict().items():
            setattr(instance, attr, value)
        await sync_to_async(instance.save)()
        return ModelGet.from_orm(instance)

    @router.patch(f"/{name}/" + "{model_id}")
    async def patch_instance(request, model_id: int, payload: ModelPost):
        """Update the model instance with the payload."""
        instance = await sync_to_async(get_object_or_404)(model, id=model_id)
        for attr, value in payload.dict().items():
            setattr(instance, attr, value)
        await sync_to_async(instance.save)()
        return ModelGet.from_orm(instance)

    @router.delete(f"/{name}/" + "{model_id}")
    async def delete_instance(request, model_id: int):
        """Delete the model instance."""
        instance = await sync_to_async(get_object_or_404)(model, id=model_id)
        await sync_to_async(instance.delete)()
        return {"success": True}

    return router


def add_model_crud_route(api, name, model):
    """Add a deafult crud router with url `name` for model `model` to the api."""
    api.add_router(f'/{name}/', _get_model_router(model, name))
