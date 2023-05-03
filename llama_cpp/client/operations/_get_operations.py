# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.5, generator: @autorest/python@6.4.11)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (ClientAuthenticationError,
                                   HttpResponseError, ResourceExistsError,
                                   ResourceNotFoundError,
                                   ResourceNotModifiedError, map_error)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer

T = TypeVar("T")
ClsType = Optional[
    Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]
]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_models_v1_models_get_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/v1/models"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


class GetOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~llama_cpp.client.LlamaCppPythonAPI`'s
        :attr:`get` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = (
            input_args.pop(0) if input_args else kwargs.pop("deserializer")
        )

    @distributed_trace
    def models_v1_models_get(self, **kwargs: Any) -> _models.ModelList:
        """Get Models.

        Get Models.

        :return: ModelList
        :rtype: ~llama_cpp.client.models.ModelList
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ModelList] = kwargs.pop("cls", None)

        request = build_models_v1_models_get_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = (
            self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("ModelList", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
