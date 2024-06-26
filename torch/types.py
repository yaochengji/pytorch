# mypy: allow-untyped-defs

# In some cases, these basic types are shadowed by corresponding
# top-level values.  The underscore variants let us refer to these
# types.  See https://github.com/python/mypy/issues/4146 for why these
# workarounds is necessary
from builtins import (  # noqa: F401
    bool as _bool,
    bytes as _bytes,
    complex as _complex,
    float as _float,
    int as _int,
    str as _str,
)
from typing import Any, List, Optional, Sequence, Tuple, TYPE_CHECKING, Union

import torch


if TYPE_CHECKING:
    from torch.autograd.graph import GradientEdge


# Convenience aliases for common composite types that we need
# to talk about in PyTorch

_TensorOrTensors = Union[torch.Tensor, Sequence[torch.Tensor]]
_TensorOrTensorsOrGradEdge = Union[
    torch.Tensor,
    Sequence[torch.Tensor],
    "GradientEdge",
    Sequence["GradientEdge"],
]

_dtype = torch.dtype
_device = torch.device
_qscheme = torch.qscheme
_layout = torch.layout
_size = Union[torch.Size, List[_int], Tuple[_int, ...]]
_dispatchkey = Union[_str, torch._C.DispatchKey]

# Meta-type for "numeric" things; matches our docs
Number = Union[_int, _float, _bool]

# Meta-type for "device-like" things.  Not to be confused with 'device' (a
# literal device object).  This nomenclature is consistent with PythonArgParser.
# None means use the default device (typically CPU)
Device = Optional[Union[_device, _str, _int]]
del Optional

# Storage protocol implemented by ${Type}StorageBase classes


class Storage:
    _cdata: _int
    device: torch.device
    dtype: torch.dtype
    _torch_load_uninitialized: _bool

    def __deepcopy__(self, memo: dict) -> "Storage":  # type: ignore[empty-body]
        ...

    def _new_shared(self, size: _int) -> "Storage":  # type: ignore[empty-body]
        ...

    def _write_file(
        self,
        f: Any,
        is_real_file: _bool,
        save_size: _bool,
        element_size: _int,
    ) -> None:
        ...

    def element_size(self) -> _int:  # type: ignore[empty-body]
        ...

    def is_shared(self) -> _bool:  # type: ignore[empty-body]
        ...

    def share_memory_(self) -> "Storage":  # type: ignore[empty-body]
        ...

    def nbytes(self) -> _int:  # type: ignore[empty-body]
        ...

    def cpu(self) -> "Storage":  # type: ignore[empty-body]
        ...

    def data_ptr(self) -> _int:  # type: ignore[empty-body]
        ...

    def from_file(  # type: ignore[empty-body]
        self,
        filename: _str,
        shared: _bool = False,
        nbytes: _int = 0,
    ) -> "Storage":
        ...

    def _new_with_file(  # type: ignore[empty-body]
        self,
        f: Any,
        element_size: _int,
    ) -> "Storage":
        ...
